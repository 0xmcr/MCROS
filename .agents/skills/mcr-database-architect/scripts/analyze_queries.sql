-- =============================================================================
-- MCR PostgreSQL Performance & Index Health Diagnostic Script
-- =============================================================================

-- 1. Identify Slow Queries (requires pg_stat_statements)
SELECT 
    round((total_exec_time / 1000 / 60)::numeric, 2) AS total_minutes,
    calls,
    round((mean_exec_time)::numeric, 2) AS mean_ms,
    query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;

-- 2. Detect Missing Indexes on Foreign Keys (Causes Seq Scans during JOIN / DELETE)
SELECT
    c.conrelid::regclass AS table_with_foreign_key,
    string_agg(att.attname, ', ') AS fk_columns,
    c.conname AS constraint_name
FROM pg_constraint c
JOIN pg_attribute att ON att.attrelid = c.conrelid AND att.attnum = ANY(c.conkey)
WHERE c.contype = 'f'
  AND NOT EXISTS (
      SELECT 1 FROM pg_index i
      WHERE i.indrelid = c.conrelid
        AND c.conkey = (i.indkey::smallint[])[1:array_length(c.conkey, 1)]
  )
GROUP BY c.conrelid, c.conname;

-- 3. Check for Unused Indexes (Wasting Disk I/O on Writes)
SELECT
    schemaname || '.' || relname AS table_name,
    indexrelname AS index_name,
    idx_scan AS index_scans,
    pg_size_pretty(pg_relation_size(indexrelid)) AS index_size
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND indisunique IS FALSE
ORDER BY pg_relation_size(indexrelid) DESC;

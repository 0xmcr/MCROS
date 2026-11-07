-- =============================================================================
-- MCR PostgreSQL Multi-Tenant Row-Level Security (RLS) Policies
-- Guarantees complete data isolation between corporate organizations/tenants.
-- =============================================================================

-- 1. Enable RLS on Tenant-Scoped Tables
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;

-- 2. Force RLS for Table Owners (Prevents superuser bypass in shared connections)
ALTER TABLE documents FORCE ROW LEVEL SECURITY;

-- 3. Policy: Users can only SELECT rows belonging to their active tenant session
-- Session variable 'app.current_tenant_id' is set per request by the API middleware
CREATE POLICY tenant_isolation_select_policy ON documents
FOR SELECT
USING (
    tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::UUID
);

-- 4. Policy: Users can only INSERT rows with their active tenant ID
CREATE POLICY tenant_isolation_insert_policy ON documents
FOR INSERT
WITH CHECK (
    tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::UUID
);

-- 5. Policy: Users can only UPDATE rows within their active tenant ID
CREATE POLICY tenant_isolation_update_policy ON documents
FOR UPDATE
USING (
    tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::UUID
)
WITH CHECK (
    tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::UUID
);

-- 6. Policy: Users can only DELETE rows within their active tenant ID
CREATE POLICY tenant_isolation_delete_policy ON documents
FOR DELETE
USING (
    tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::UUID
);

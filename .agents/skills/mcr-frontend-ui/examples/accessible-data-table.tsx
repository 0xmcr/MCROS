/**
 * @file accessible-data-table.tsx
 * @description Production-ready, WCAG 2.1 AA compliant data table component in React & Tailwind CSS.
 * Handles all 4 component visual states: Loading (skeleton), Error (retry), Empty, and Settled.
 */

import React from "react";

export interface Column<T> {
  key: string;
  header: string;
  render?: (item: T) => React.ReactNode;
}

export interface DataTableProps<T> {
  columns: Column<T>[];
  data: T[] | null;
  isLoading: boolean;
  error: Error | null;
  onRetry?: () => void;
  emptyMessage?: string;
}

export function DataTable<T extends { id: string | number }>({
  columns,
  data,
  isLoading,
  error,
  onRetry,
  emptyMessage = "No records found.",
}: DataTableProps<T>) {
  // 1. Error State
  if (error) {
    return (
      <div 
        role="alert" 
        className="rounded-lg border border-red-500/20 bg-red-500/10 p-6 text-center text-red-600 dark:text-red-400"
      >
        <p className="font-medium">Failed to load data: {error.message}</p>
        {onRetry && (
          <button
            onClick={onRetry}
            className="mt-4 inline-flex items-center rounded-md bg-red-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-red-600 focus:ring-offset-2 active:scale-95 transition-all"
          >
            Retry Request
          </button>
        )}
      </div>
    );
  }

  // 2. Loading State (Skeleton preserving geometry to eliminate CLS)
  if (isLoading) {
    return (
      <div className="w-full overflow-hidden rounded-lg border border-slate-200 dark:border-slate-800 animate-pulse">
        <div className="h-12 bg-slate-100 dark:bg-slate-800 border-b border-slate-200 dark:border-slate-700" />
        {[...Array(5)].map((_, i) => (
          <div key={i} className="flex h-16 items-center border-b border-slate-100 dark:border-slate-800/50 px-4">
            <div className="h-4 w-3/4 bg-slate-200 dark:bg-slate-700 rounded" />
          </div>
        ))}
      </div>
    );
  }

  // 3. Empty State
  if (!data || data.length === 0) {
    return (
      <div className="rounded-lg border border-dashed border-slate-300 dark:border-slate-700 p-12 text-center text-slate-500 dark:text-slate-400">
        <p className="text-base font-medium">{emptyMessage}</p>
      </div>
    );
  }

  // 4. Settled / Success State
  return (
    <div className="w-full overflow-x-auto rounded-lg border border-slate-200 dark:border-slate-800 shadow-sm">
      <table className="w-full text-left text-sm text-slate-700 dark:text-slate-300">
        <thead className="bg-slate-50 dark:bg-slate-900/50 text-xs uppercase text-slate-500 dark:text-slate-400 border-b border-slate-200 dark:border-slate-800">
          <tr>
            {columns.map((col) => (
              <th key={col.key} scope="col" className="px-6 py-3 font-semibold">
                {col.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
          {data.map((item) => (
            <tr key={item.id} className="hover:bg-slate-50/50 dark:hover:bg-slate-800/50 transition-colors">
              {columns.map((col) => (
                <td key={col.key} className="px-6 py-4 whitespace-nowrap">
                  {col.render ? col.render(item) : (item as any)[col.key]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

import { Suspense } from "react";
import { Outlet } from "react-router-dom";

/**
 * Creator experience shell — follows YouTube dashboard conventions.
 */
export function CreatorLayout() {
  return (
    <div className="theme-creator min-h-dvh bg-background">
      <Suspense fallback={<div className="p-6 text-sm">Loading…</div>}>
        <Outlet />
      </Suspense>
    </div>
  );
}

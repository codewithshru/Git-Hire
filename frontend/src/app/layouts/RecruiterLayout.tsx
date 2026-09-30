import { Suspense } from "react";
import { Outlet } from "react-router-dom";

/**
 * Recruiter experience shell — desktop-first, green theme.
 * Sidebar navigation (Home · Search · Post Job · Messages · Profile) is added
 * with the recruiter feature modules.
 */
export function RecruiterLayout() {
  return (
    <div className="theme-recruiter min-h-dvh bg-background">
      <Suspense fallback={<div className="p-6 text-sm">Loading…</div>}>
        <Outlet />
      </Suspense>
    </div>
  );
}

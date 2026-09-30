import { Suspense } from "react";
import { Outlet } from "react-router-dom";

/**
 * Candidate experience shell — mobile-first, indigo/purple theme.
 * Bottom navigation (Home · Explore · Create · Jobs · Connect) is added
 * with the candidate feature modules.
 */
export function CandidateLayout() {
  return (
    <div className="theme-candidate min-h-dvh bg-background">
      <Suspense fallback={<div className="p-6 text-sm">Loading…</div>}>
        <Outlet />
      </Suspense>
    </div>
  );
}

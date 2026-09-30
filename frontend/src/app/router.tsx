import { lazy, Suspense } from "react";
import { createBrowserRouter, Navigate } from "react-router-dom";
import { CandidateLayout } from "./layouts/CandidateLayout";
import { RecruiterLayout } from "./layouts/RecruiterLayout";
import { CreatorLayout } from "./layouts/CreatorLayout";

/** Experiences are code-split: users only download the role they use. */
const CandidateHome = lazy(() => import("@/modules/candidate/pages/Home"));
const RecruiterHome = lazy(() => import("@/modules/recruiter/pages"));
const CreatorDashboard = lazy(() => import("@/modules/creator/pages/Dashboard"));

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Navigate to="/candidate" replace />,
  },
  {
    path: "/candidate",
    element: <CandidateLayout />,
    children: [
      { index: true, element: <Suspense><CandidateHome /></Suspense> },
    ],
  },
  {
    path: "/recruiter",
    element: <RecruiterLayout />,
    children: [
      { index: true, element: <Suspense><RecruiterHome /></Suspense> },
    ],
  },
  {
    path: "/creator",
    element: <CreatorLayout />,
    children: [
      { index: true, element: <Suspense><CreatorDashboard /></Suspense> },
    ],
  },
]);

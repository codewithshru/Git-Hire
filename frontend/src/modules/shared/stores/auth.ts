import { create } from "zustand";

/**
 * Client-side auth session state (tokens/user id).
 *
 * Ownership rule: server data lives in TanStack Query — this store only holds
 * the auth session and UI preferences that must survive across pages.
 */
export type Role = "candidate" | "recruiter" | "creator";

interface AuthState {
  accessToken: string | null;
  role: Role | null;
  setSession: (accessToken: string | null, role: Role | null) => void;
  clearSession: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  accessToken: null,
  role: null,
  setSession: (accessToken, role) => set({ accessToken, role }),
  clearSession: () => set({ accessToken: null, role: null }),
}));

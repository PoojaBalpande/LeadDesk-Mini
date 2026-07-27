"use client";

import { useReveal } from "@/hooks/useReveal";

/**
 * Client wrapper to initialize IntersectionObserver scroll reveal for landing page sections.
 */
export function ScrollReveal({ children }: { children: React.ReactNode }) {
  useReveal();
  return <>{children}</>;
}

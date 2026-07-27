"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { Container } from "./Container";
import { Logo } from "@/components/common/Logo";
import { Button } from "@/components/common/Button";
import { ThemeToggle } from "@/components/common/ThemeToggle";
import { NAV_ITEMS } from "@/lib/navigation";
import { cn } from "@/lib/utils";

/**
 * Responsive Floating Sticky Navbar Layout Component
 * Restyled with scroll awareness, backdrop blur, semantic tokens, and ThemeToggle.
 */
export function Navbar() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 10);
    };

    handleScroll();
    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <header className="sticky top-[var(--layout-nav-inset)] z-[var(--z-nav)] w-full py-2 transition-all duration-[var(--duration-base)] ease-[var(--ease-standard)]">
      <Container>
        <div
          className={cn(
            "flex h-[var(--layout-nav-height)] items-center justify-between rounded-2xl border px-4 sm:px-6 backdrop-blur-md transition-all duration-[var(--duration-base)] ease-[var(--ease-standard)]",
            scrolled
              ? "border-border bg-surface/90 shadow-md"
              : "border-border/80 bg-surface/75 shadow-sm"
          )}
        >
          {/* Brand Logo */}
          <Logo />

          {/* Configuration-driven Navigation Links */}
          <nav
            aria-label="Main Navigation"
            className="hidden items-center gap-8 md:flex"
          >
            {NAV_ITEMS.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="text-sm font-medium text-body transition-colors hover:text-heading focus-visible:outline-none"
              >
                {item.label}
              </Link>
            ))}
          </nav>

          {/* Action CTAs */}
          <div className="flex items-center gap-3">
            <ThemeToggle />
            <Button href="/login" variant="primary" size="sm">
              Admin Login
            </Button>
          </div>
        </div>
      </Container>
    </header>
  );
}

import Link from "next/link";
import { Container } from "./Container";
import { Logo } from "@/components/common/Logo";
import { SITE_CONFIG } from "@/lib/constants";
import { NAV_ITEMS } from "@/lib/navigation";

/**
 * Reusable Footer Layout Component
 * Converted strictly to semantic tokens (bg-surface, text-body, text-muted, border-border).
 */
export function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="border-t border-border bg-surface py-12 text-body">
      <Container>
        <div className="flex flex-col items-center justify-between gap-8 md:flex-row md:items-start">
          {/* Logo & Description */}
          <div className="flex max-w-sm flex-col gap-3 text-center md:text-left">
            <Logo />
            <p className="text-sm leading-relaxed text-muted">
              {SITE_CONFIG.description}
            </p>
          </div>

          {/* Configuration-driven Navigation Links */}
          <nav
            aria-label="Footer Navigation"
            className="flex flex-wrap justify-center gap-6 text-sm font-medium text-body"
          >
            {NAV_ITEMS.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="transition-colors hover:text-heading focus-visible:outline-none"
              >
                {item.label}
              </Link>
            ))}
          </nav>
        </div>

        {/* Divider & Copyright */}
        <div className="mt-8 flex flex-col items-center justify-between gap-4 border-t border-border pt-8 text-center text-xs text-muted sm:flex-row">
          <p>
            © {currentYear} {SITE_CONFIG.name}. All rights reserved.
          </p>

          {/* Digital Heroes Attribution Requirement */}
          <p>
            <a
              href={SITE_CONFIG.attribution.url}
              target="_blank"
              rel="noopener noreferrer"
              className="font-medium text-heading underline-offset-4 transition-colors hover:underline focus-visible:outline-none"
            >
              {SITE_CONFIG.attribution.text}
            </a>
          </p>
        </div>
      </Container>
    </footer>
  );
}

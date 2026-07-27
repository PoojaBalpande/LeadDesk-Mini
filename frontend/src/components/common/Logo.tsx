import Link from "next/link";
import { SITE_CONFIG } from "@/lib/constants";
import { cn } from "@/lib/utils";

interface LogoProps {
  className?: string;
}

/**
 * Text Logo Component
 */
export function Logo({ className }: LogoProps) {
  return (
    <Link
      href="/"
      className={cn(
        "flex items-center gap-2 text-xl font-extrabold tracking-tight text-heading transition-opacity hover:opacity-90",
        className
      )}
    >
      <span className="flex h-8 w-8 items-center justify-center rounded-2xl bg-primary text-sm font-bold text-primary-foreground shadow-sm">
        LM
      </span>
      <span>{SITE_CONFIG.name}</span>
    </Link>
  );
}

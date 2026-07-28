import Link from "next/link";
import { ButtonProps } from "@/types";
import { cn } from "@/lib/utils";

/**
 * Reusable Button Component
 * Supports variants (primary, secondary, outline), sizes, disabled states, and link wrapper.
 */
export function Button({
  children,
  variant = "primary",
  size = "md",
  type = "button",
  disabled = false,
  className,
  href,
  onClick,
}: ButtonProps) {
  const baseStyles =
    "inline-flex items-center justify-center font-semibold rounded-full transition-all duration-[var(--duration-base)] ease-[var(--ease-standard)] focus-visible:outline-none disabled:pointer-events-none disabled:opacity-[var(--opacity-disabled)] active:scale-[0.98]";

  const variantStyles = {
    primary: "bg-primary text-primary-foreground shadow-sm hover:opacity-90",
    secondary: "bg-heading text-background shadow-sm hover:opacity-90",
    outline:
      "border border-border bg-surface text-heading shadow-sm hover:bg-accent",
  };

  const sizeStyles = {
    sm: "px-3 py-1.5 text-xs",
    md: "px-4 py-2 text-sm",
    lg: "px-5 py-2.5 text-base",
  };

  const combinedClasses = cn(
    baseStyles,
    variantStyles[variant],
    sizeStyles[size],
    className
  );

  if (href) {
    return (
      <Link href={href} className={combinedClasses}>
        {children}
      </Link>
    );
  }

  return (
    <button
      type={type}
      disabled={disabled}
      onClick={onClick}
      className={combinedClasses}
    >
      {children}
    </button>
  );
}

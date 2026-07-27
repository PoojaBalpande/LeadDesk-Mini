import { BadgeProps } from "@/types";
import { cn } from "@/lib/utils";

/**
 * Reusable Badge Component
 */
export function Badge({
  children,
  variant = "default",
  className,
}: BadgeProps) {
  const variantStyles = {
    default: "bg-primary/20 text-heading ring-1 ring-inset ring-primary/30",
    outline: "bg-surface text-body ring-1 ring-inset ring-border",
    success: "bg-success/20 text-heading ring-1 ring-inset ring-success/40",
  };

  return (
    <span
      className={cn(
        "inline-flex items-center gap-x-1.5 rounded-full px-3 py-1 text-xs font-semibold uppercase tracking-wider transition-colors",
        variantStyles[variant],
        className
      )}
    >
      {children}
    </span>
  );
}

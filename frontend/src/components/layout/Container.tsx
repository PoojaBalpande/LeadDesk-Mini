import { ContainerProps } from "@/types";
import { cn } from "@/lib/utils";

/**
 * Reusable Container Component
 * Encapsulates max-width, responsive padding, and centering across all page layout sections.
 */
export function Container({
  children,
  className,
  as: Component = "div",
}: ContainerProps) {
  return (
    <Component
      className={cn(
        "mx-auto w-full max-w-[var(--layout-max-width)] px-[var(--space-page-gutter)]",
        className
      )}
    >
      {children}
    </Component>
  );
}

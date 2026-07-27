import { SurfaceProps } from "@/types";
import { cn } from "@/lib/utils";

const variantStyles = {
  section: "bg-section border border-border shadow-sm",
  surface: "bg-surface border border-border shadow-sm",
  accent: "bg-section border border-border shadow-md",
  transparent: "bg-transparent border-transparent shadow-none",
} as const;

export function Surface({
  children,
  variant = "section",
  className,
  as: Component = "div",
  hover = false,
}: SurfaceProps) {
  return (
    <Component
      className={cn(
        "rounded-3xl",
        variantStyles[variant],
        hover &&
          "transition-[box-shadow,transform] duration-[var(--duration-base)] ease-[var(--ease-standard)] hover:[transform:translateY(-2px)] hover:shadow-md",
        className
      )}
    >
      {children}
    </Component>
  );
}

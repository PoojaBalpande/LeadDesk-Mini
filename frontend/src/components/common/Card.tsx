import { CardProps } from "@/types";
import { cn } from "@/lib/utils";

/**
 * Reusable Card Component
 */
export function Card({
  title,
  description,
  icon,
  children,
  className,
}: CardProps) {
  return (
    <div
      className={cn(
        "rounded-3xl border border-border bg-card p-6 shadow-sm",
        "transition-[box-shadow,transform] duration-[var(--duration-base)] ease-[var(--ease-standard)]",
        "hover:[transform:translateY(-2px)] hover:shadow-md",
        className
      )}
    >
      {icon && (
        <div className="mb-4 inline-flex h-10 w-10 items-center justify-center rounded-2xl bg-primary text-primary-foreground">
          {icon}
        </div>
      )}
      {title && <h3 className="text-heading">{title}</h3>}
      {description && (
        <p className="mt-2 text-sm leading-[var(--leading-body)] text-body">
          {description}
        </p>
      )}
      {children && <div className="mt-4">{children}</div>}
    </div>
  );
}

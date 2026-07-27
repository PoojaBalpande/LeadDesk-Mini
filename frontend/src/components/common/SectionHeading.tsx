import { SectionHeadingProps } from "@/types";
import { Badge } from "./Badge";
import { cn } from "@/lib/utils";

/**
 * Reusable Section Heading Component
 * Supports eyebrow badge, title, description, and left/center/right alignment.
 */
export function SectionHeading({
  eyebrow,
  title,
  description,
  alignment = "center",
  className,
}: SectionHeadingProps) {
  const alignmentStyles = {
    left: "text-left items-start",
    center: "text-center items-center mx-auto",
    right: "text-right items-end ml-auto",
  };

  return (
    <div
      className={cn(
        "flex max-w-3xl flex-col gap-3",
        alignmentStyles[alignment],
        className
      )}
    >
      {eyebrow && <Badge>{eyebrow}</Badge>}
      <h2 className="text-3xl font-extrabold tracking-tight text-heading sm:text-4xl">
        {title}
      </h2>
      {description && (
        <p className="text-lg leading-[var(--leading-body)] text-body">
          {description}
        </p>
      )}
    </div>
  );
}

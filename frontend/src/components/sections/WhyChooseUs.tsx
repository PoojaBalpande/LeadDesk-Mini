import { Container } from "@/components/layout/Container";
import { SectionHeading } from "@/components/common/SectionHeading";
import { Card } from "@/components/common/Card";
import { SECTION_IDS } from "@/lib/constants";
import { SectionProps } from "@/types";
import { ShieldCheck, Cpu, Sparkles } from "lucide-react";

const VALUE_PROPS = [
  {
    title: "Zero Bloatware",
    description:
      "Engineered with clean architecture and lightweight components to keep load times lightning fast.",
    icon: <Cpu className="h-5 w-5" aria-hidden="true" />,
  },
  {
    title: "Realtime Pipeline",
    description:
      "Instant visibility into incoming inquiries with synchronized status transitions across your team.",
    icon: <Sparkles className="h-5 w-5" aria-hidden="true" />,
  },
  {
    title: "Production Ready",
    description:
      "Configured with strict API schemas, Zod validation, and dark mode support out of the box.",
    icon: <ShieldCheck className="h-5 w-5" aria-hidden="true" />,
  },
];

/**
 * Restyled WhyChooseUs Section Component
 * Features value proposition cards with semantic tokens, SectionHeading, and reveal support.
 */
export function WhyChooseUs({
  id = SECTION_IDS.whyChooseUs,
  className = "",
}: Partial<SectionProps>) {
  return (
    <section
      id={id}
      className={`reveal py-[var(--space-section-y)] ${className}`}
    >
      <Container>
        <SectionHeading
          eyebrow="Why LeadDesk Mini"
          title="Designed for Performance & Simplicity"
          description="Zero fluff. Just clean architecture, modern performance, and reliable lead processing."
        />

        <div className="mt-12 grid grid-cols-1 gap-8 md:grid-cols-3">
          {VALUE_PROPS.map((prop, idx) => (
            <Card
              key={idx}
              title={prop.title}
              description={prop.description}
              icon={prop.icon}
            />
          ))}
        </div>
      </Container>
    </section>
  );
}

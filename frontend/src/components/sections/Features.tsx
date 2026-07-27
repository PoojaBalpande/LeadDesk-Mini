import { Container } from "@/components/layout/Container";
import { SectionHeading } from "@/components/common/SectionHeading";
import { Card } from "@/components/common/Card";
import { SECTION_IDS } from "@/lib/constants";
import { SectionProps } from "@/types";
import { Zap, BarChart3, Search } from "lucide-react";

const FEATURE_ITEMS = [
  {
    title: "Instant Lead Capture",
    description:
      "Public landing page forms configured with strict validation to ingest business inquiries seamlessly.",
    icon: <Zap className="h-5 w-5" aria-hidden="true" />,
  },
  {
    title: "Status Tracking Pipeline",
    description:
      "Transition lead states between NEW, CONTACTED, and CLOSED in an intuitive admin dashboard.",
    icon: <BarChart3 className="h-5 w-5" aria-hidden="true" />,
  },
  {
    title: "Search & Filter Engine",
    description:
      "Query leads instantly by name, email, budget brackets, or status tags.",
    icon: <Search className="h-5 w-5" aria-hidden="true" />,
  },
];

/**
 * Restyled Features Section Component
 * Consumes Cards with icons, semantic spacing tokens, and reveal support.
 */
export function Features({
  id = SECTION_IDS.features,
  className = "",
}: Partial<SectionProps>) {
  return (
    <section
      id={id}
      className={`reveal py-[var(--space-section-y)] ${className}`}
    >
      <Container>
        <SectionHeading
          eyebrow="Core Features"
          title="Everything You Need to Manage Inquiries"
          description="Built from the ground up for clarity, speed, and production reliability."
        />
        <div className="mt-12 grid grid-cols-1 gap-8 md:grid-cols-3">
          {FEATURE_ITEMS.map((item, idx) => (
            <Card
              key={idx}
              title={item.title}
              description={item.description}
              icon={item.icon}
            />
          ))}
        </div>
      </Container>
    </section>
  );
}

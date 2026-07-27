import { Container } from "@/components/layout/Container";
import { SectionHeading } from "@/components/common/SectionHeading";
import { Surface } from "@/components/common/Surface";
import { Badge } from "@/components/common/Badge";
import { SECTION_IDS } from "@/lib/constants";
import { SectionProps } from "@/types";

const STEPS = [
  {
    step: "01",
    title: "Visitor Submits Form",
    desc: "Leads enter details on the landing page with real-time validation.",
  },
  {
    step: "02",
    title: "Instant DB Storage",
    desc: "Validated inquiry data is securely stored in PostgreSQL.",
  },
  {
    step: "03",
    title: "Admin Management",
    desc: "Admins review, update status, and close deals effortlessly.",
  },
];

/**
 * Restyled HowItWorks Section Component
 * Consumes Surface step cards, Badge, semantic tokens, and reveal support.
 */
export function HowItWorks({
  id = SECTION_IDS.howItWorks,
  className = "",
}: Partial<SectionProps>) {
  return (
    <section
      id={id}
      className={`reveal py-[var(--space-section-y)] ${className}`}
    >
      <Container>
        <SectionHeading
          eyebrow="Workflow"
          title="3 Steps to Streamlining Your Pipeline"
          description="How LeadDesk Mini handles incoming inquiries from capture to closure."
        />
        <div className="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-3">
          {STEPS.map((item, idx) => (
            <Surface
              key={idx}
              variant="surface"
              hover
              className="flex flex-col items-center p-6 text-center"
            >
              <Badge variant="default" className="mb-3">
                Step {item.step}
              </Badge>
              <h3 className="text-base font-semibold text-heading">
                {item.title}
              </h3>
              <p className="mt-2 text-xs leading-[var(--leading-body)] text-body">
                {item.desc}
              </p>
            </Surface>
          ))}
        </div>
      </Container>
    </section>
  );
}

import { Container } from "@/components/layout/Container";
import { Button } from "@/components/common/Button";
import { Surface } from "@/components/common/Surface";
import { SECTION_IDS } from "@/lib/constants";
import { SectionProps } from "@/types";

/**
 * Restyled Call to Action Section Component
 * Features exact specified copy, exact button labels, semantic Surface styling, and reveal support.
 */
export function CTA({
  id = SECTION_IDS.cta,
  className = "",
}: Partial<SectionProps>) {
  return (
    <section
      id={id}
      className={`reveal py-[var(--space-section-y)] ${className}`}
    >
      <Container>
        <Surface
          variant="accent"
          className="flex flex-col items-center px-6 py-14 text-center shadow-lg sm:px-12 sm:py-16"
        >
          <h2 className="max-w-2xl text-h2 font-extrabold text-heading">
            Ready to take control of your lead pipeline?
          </h2>
          <p className="mt-4 max-w-lg text-body-lg text-body">
            Start capturing qualified inquiries today with LeadDesk Mini.
          </p>
          <div className="mt-8 flex flex-wrap justify-center gap-4">
            <Button
              href={`#${SECTION_IDS.contact}`}
              variant="primary"
              size="lg"
            >
              Submit an inquiry
            </Button>
            <Button href="/login" variant="outline" size="lg">
              Open admin portal
            </Button>
          </div>
        </Surface>
      </Container>
    </section>
  );
}

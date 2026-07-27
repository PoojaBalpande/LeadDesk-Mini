"use client";

import { Container } from "@/components/layout/Container";
import { SectionHeading } from "@/components/common/SectionHeading";
import { Surface } from "@/components/common/Surface";
import { Button } from "@/components/common/Button";
import { SECTION_IDS } from "@/lib/constants";
import { SectionProps } from "@/types";

/**
 * Restyled Contact & Lead Capture Section Component
 * Features token-based form styling, exact 'Send inquiry' button label, and reveal support.
 */
export function Contact({
  id = SECTION_IDS.contact,
  className = "",
}: Partial<SectionProps>) {
  return (
    <section
      id={id}
      className={`reveal py-[var(--space-section-y)] ${className}`}
    >
      <Container>
        <SectionHeading
          eyebrow="Get In Touch"
          title="Submit a Business Inquiry"
          description="Fill out the form below to connect with our team and accelerate your sales pipeline."
        />

        <div className="mx-auto mt-12 max-w-xl">
          <Surface variant="surface" className="p-6 sm:p-8">
            <form
              onSubmit={(e) => e.preventDefault()}
              className="flex flex-col gap-4"
            >
              <div>
                <label
                  htmlFor="contact-name"
                  className="mb-1.5 block text-xs font-semibold text-heading"
                >
                  Full Name
                </label>
                <input
                  id="contact-name"
                  type="text"
                  placeholder="Jane Doe"
                  className="w-full rounded-2xl border border-border bg-background px-4 py-2.5 text-sm text-heading placeholder:text-muted transition-colors focus:outline-none focus:ring-2 focus:ring-ring"
                />
              </div>

              <div>
                <label
                  htmlFor="contact-email"
                  className="mb-1.5 block text-xs font-semibold text-heading"
                >
                  Work Email
                </label>
                <input
                  id="contact-email"
                  type="email"
                  placeholder="jane@company.com"
                  className="w-full rounded-2xl border border-border bg-background px-4 py-2.5 text-sm text-heading placeholder:text-muted transition-colors focus:outline-none focus:ring-2 focus:ring-ring"
                />
              </div>

              <div>
                <label
                  htmlFor="contact-budget"
                  className="mb-1.5 block text-xs font-semibold text-heading"
                >
                  Estimated Budget
                </label>
                <select
                  id="contact-budget"
                  className="w-full rounded-2xl border border-border bg-background px-4 py-2.5 text-sm text-heading transition-colors focus:outline-none focus:ring-2 focus:ring-ring"
                  defaultValue="$15,000 – $50,000"
                >
                  <option value="$5,000 – $15,000">$5,000 – $15,000</option>
                  <option value="$15,000 – $50,000">$15,000 – $50,000</option>
                  <option value="$50,000+">$50,000+</option>
                </select>
              </div>

              <div>
                <label
                  htmlFor="contact-message"
                  className="mb-1.5 block text-xs font-semibold text-heading"
                >
                  Project Details
                </label>
                <textarea
                  id="contact-message"
                  rows={3}
                  placeholder="Tell us about your lead volume and timeline..."
                  className="w-full rounded-2xl border border-border bg-background px-4 py-2.5 text-sm text-heading placeholder:text-muted transition-colors focus:outline-none focus:ring-2 focus:ring-ring"
                />
              </div>

              <div className="mt-2">
                <Button
                  type="submit"
                  variant="primary"
                  size="lg"
                  className="w-full"
                >
                  Send inquiry
                </Button>
              </div>
            </form>
          </Surface>
        </div>
      </Container>
    </section>
  );
}

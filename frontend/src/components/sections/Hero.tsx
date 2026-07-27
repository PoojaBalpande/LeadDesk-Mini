import { Container } from "@/components/layout/Container";
import { Badge } from "@/components/common/Badge";
import { Button } from "@/components/common/Button";
import { Surface } from "@/components/common/Surface";
import { SECTION_IDS } from "@/lib/constants";
import { SectionProps } from "@/types";

/**
 * Premium Hero Section Component
 * Features a 45/55 split on desktop, pure CSS pipeline mockup with status tokens,
 * decorative blurred blobs, and a trust strip.
 */
export function Hero({
  id = SECTION_IDS.hero,
  className = "",
}: Partial<SectionProps>) {
  return (
    <section
      id={id}
      className={`relative overflow-hidden py-16 sm:py-24 lg:py-28 ${className}`}
    >
      {/* Decorative blurred CSS background blobs */}
      <div
        className="pointer-events-none absolute -top-24 left-1/2 -z-10 h-[500px] w-[500px] -translate-x-1/2 rounded-full bg-primary/25 blur-3xl"
        aria-hidden="true"
      />
      <div
        className="pointer-events-none absolute -bottom-16 right-0 -z-10 h-[380px] w-[380px] rounded-full bg-accent/40 blur-3xl"
        aria-hidden="true"
      />

      <Container>
        {/* 45 / 55 Split Layout */}
        <div className="grid grid-cols-1 items-center gap-12 lg:grid-cols-12 lg:gap-8">
          {/* Left Column — 45% split (5 of 12 columns) */}
          <div className="flex flex-col items-start text-left lg:col-span-5">
            <Badge variant="default" className="mb-4">
              LeadDesk Mini
            </Badge>

            <h1 className="text-display font-extrabold leading-[var(--leading-display)] text-heading">
              Capture, organize, and close leads without the clutter
            </h1>

            <p className="mt-6 text-body-lg leading-[var(--leading-body)] text-body">
              LeadDesk Mini gives scaling businesses a modern pipeline to capture
              inquiries from high-converting landing pages and process them in
              real-time.
            </p>

            <div className="mt-8 flex flex-wrap items-center gap-4">
              <Button href={`#${SECTION_IDS.contact}`} variant="primary" size="lg">
                Start free inquiry
              </Button>

              <Button
                href={`#${SECTION_IDS.howItWorks}`}
                variant="outline"
                size="lg"
              >
                See how it works
              </Button>
            </div>
          </div>

          {/* Right Column — 55% split (7 of 12 columns) — Pure CSS Dashboard Mockup */}
          <div className="lg:col-span-7">
            <Surface
              variant="surface"
              className="relative overflow-hidden p-4 sm:p-6 shadow-lg"
            >
              {/* Mockup Header */}
              <div className="mb-4 flex items-center justify-between border-b border-border/80 pb-3">
                <div className="flex items-center gap-2">
                  <div className="h-3 w-3 rounded-full bg-success" />
                  <span className="text-xs font-bold uppercase tracking-wider text-heading">
                    Live Lead Pipeline
                  </span>
                </div>
                <div className="flex items-center gap-1.5 text-xs text-muted">
                  <span className="inline-block h-2 w-2 rounded-full bg-primary animate-pulse" />
                  Realtime updates active
                </div>
              </div>

              {/* 4 Pipeline Status Columns */}
              <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-4">
                {/* Column 1: New Leads */}
                <div className="flex flex-col gap-2.5 rounded-2xl border border-border/60 bg-section/40 p-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-heading">New Leads</span>
                    <span className="rounded-full bg-info/20 px-2 py-0.5 text-[10px] font-bold text-info-foreground">
                      2
                    </span>
                  </div>
                  <div className="rounded-xl border border-border bg-card p-3 shadow-sm transition-transform hover:-translate-y-0.5">
                    <div className="text-xs font-semibold text-heading">Acme Corp</div>
                    <div className="mt-1 text-[11px] text-muted">$12,400 • Enterprise</div>
                    <div className="mt-2 text-[10px] text-body">2 mins ago</div>
                  </div>
                  <div className="rounded-xl border border-border bg-card p-3 shadow-sm transition-transform hover:-translate-y-0.5">
                    <div className="text-xs font-semibold text-heading">Nexus Design</div>
                    <div className="mt-1 text-[11px] text-muted">$8,500 • Starter</div>
                    <div className="mt-2 text-[10px] text-body">15 mins ago</div>
                  </div>
                </div>

                {/* Column 2: Qualified */}
                <div className="flex flex-col gap-2.5 rounded-2xl border border-border/60 bg-section/40 p-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-heading">Qualified</span>
                    <span className="rounded-full bg-qualified/20 px-2 py-0.5 text-[10px] font-bold text-qualified-foreground">
                      1
                    </span>
                  </div>
                  <div className="rounded-xl border border-border bg-card p-3 shadow-sm transition-transform hover:-translate-y-0.5">
                    <div className="text-xs font-semibold text-heading">Vertex Systems</div>
                    <div className="mt-1 text-[11px] text-muted">$45,000 • Growth</div>
                    <div className="mt-2 text-[10px] text-body">1 hour ago</div>
                  </div>
                </div>

                {/* Column 3: Proposal Sent */}
                <div className="flex flex-col gap-2.5 rounded-2xl border border-border/60 bg-section/40 p-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-heading">Proposal Sent</span>
                    <span className="rounded-full bg-warning/20 px-2 py-0.5 text-[10px] font-bold text-warning-foreground">
                      1
                    </span>
                  </div>
                  <div className="rounded-xl border border-border bg-card p-3 shadow-sm transition-transform hover:-translate-y-0.5">
                    <div className="text-xs font-semibold text-heading">Nebula AI</div>
                    <div className="mt-1 text-[11px] text-muted">$88,000 • Custom</div>
                    <div className="mt-2 text-[10px] text-body">3 hours ago</div>
                  </div>
                </div>

                {/* Column 4: Won */}
                <div className="flex flex-col gap-2.5 rounded-2xl border border-border/60 bg-section/40 p-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-heading">Won</span>
                    <span className="rounded-full bg-success/20 px-2 py-0.5 text-[10px] font-bold text-success-foreground">
                      1
                    </span>
                  </div>
                  <div className="rounded-xl border border-border bg-card p-3 shadow-sm transition-transform hover:-translate-y-0.5">
                    <div className="text-xs font-semibold text-heading">Starlight Labs</div>
                    <div className="mt-1 text-[11px] text-muted">$32,500 • Pro</div>
                    <div className="mt-2 text-[10px] text-body">Just now</div>
                  </div>
                </div>
              </div>
            </Surface>
          </div>
        </div>

        {/* Trust Strip Below Hero */}
        <div className="mt-16 flex flex-wrap items-center justify-center gap-x-6 gap-y-2 border-t border-border/80 pt-8 text-center text-xs font-medium uppercase tracking-wider text-muted sm:text-sm">
          <span>Secure</span>
          <span aria-hidden="true" className="text-border">
            •
          </span>
          <span>Fast</span>
          <span aria-hidden="true" className="text-border">
            •
          </span>
          <span>Production-ready</span>
        </div>
      </Container>
    </section>
  );
}

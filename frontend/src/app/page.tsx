import { Navbar } from "@/components/layout/Navbar";
import { Footer } from "@/components/layout/Footer";
import { Hero } from "@/components/sections/Hero";
import { Features } from "@/components/sections/Features";
import { WhyChooseUs } from "@/components/sections/WhyChooseUs";
import { HowItWorks } from "@/components/sections/HowItWorks";
import { CTA } from "@/components/sections/CTA";
import { Contact } from "@/components/sections/Contact";
import { ScrollReveal } from "@/components/common/ScrollReveal";

/**
 * Public Marketing Landing Page
 * Composition-only Server Component layout adhering strictly to design tokens.
 */
export default function HomePage() {
  return (
    <div className="flex min-h-screen flex-col bg-background text-body">
      <Navbar />
      <ScrollReveal>
        <main className="flex-1">
          <Hero />
          <Features />
          <WhyChooseUs />
          <HowItWorks />
          <CTA />
          <Contact />
        </main>
      </ScrollReveal>
      <Footer />
    </div>
  );
}

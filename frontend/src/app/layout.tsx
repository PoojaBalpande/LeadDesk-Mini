import type { Metadata } from "next";
import { DM_Sans, Plus_Jakarta_Sans } from "next/font/google";
import { ThemeProvider } from "@/components/common/ThemeProvider";
import { SITE_CONFIG } from "@/lib/constants";
import "./globals.css";

const plusJakarta = Plus_Jakarta_Sans({
  subsets: ["latin"],
  variable: "--font-heading",
  display: "swap",
});

const dmSans = DM_Sans({
  subsets: ["latin"],
  variable: "--font-sans",
  display: "swap",
});

export const metadata: Metadata = {
  title: `${SITE_CONFIG.name} — Modern Lead Management`,
  description: SITE_CONFIG.description,
  applicationName: SITE_CONFIG.name,
  robots: { index: true, follow: true },
  openGraph: {
    title: `${SITE_CONFIG.name} — Modern Lead Management`,
    description: SITE_CONFIG.description,
    type: "website",
    siteName: SITE_CONFIG.name,
  },
  twitter: {
    card: "summary_large_image",
    title: `${SITE_CONFIG.name} — Modern Lead Management`,
    description: SITE_CONFIG.description,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
      className={`${plusJakarta.variable} ${dmSans.variable} h-full scroll-smooth antialiased`}
    >
      <body className="flex min-h-full flex-col bg-background font-sans text-body">
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  );
}

import { SECTION_IDS } from "./constants";
import { NavItem } from "@/types";

/**
 * Configuration-driven Navigation Items array
 */
export const NAV_ITEMS: NavItem[] = [
  {
    label: "Features",
    href: `#${SECTION_IDS.features}`,
  },
  {
    label: "Why Us",
    href: `#${SECTION_IDS.whyChooseUs}`,
  },
  {
    label: "How It Works",
    href: `#${SECTION_IDS.howItWorks}`,
  },
  {
    label: "Contact",
    href: `#${SECTION_IDS.contact}`,
  },
];

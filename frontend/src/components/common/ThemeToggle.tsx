"use client";

import { useTheme } from "next-themes";
import { useSyncExternalStore } from "react";
import { Monitor, Moon, Sun } from "lucide-react";
import { cycleTheme, type ThemeMode } from "@/lib/theme";
import { cn } from "@/lib/utils";

const ICONS = {
  light: Sun,
  dark: Moon,
  system: Monitor,
} as const;

const LABELS = {
  light: "Light",
  dark: "Dark",
  system: "System",
} as const;

const emptySubscribe = () => () => {};

export function ThemeToggle() {
  const { theme, setTheme, resolvedTheme } = useTheme();
  const mounted = useSyncExternalStore(
    emptySubscribe,
    () => true,
    () => false
  );

  const mode = (theme as ThemeMode | undefined) ?? "system";
  const Icon = mounted ? ICONS[mode] : Monitor;

  return (
    <button
      type="button"
      aria-label={`Theme: ${LABELS[mode]}. Click to switch to ${LABELS[cycleTheme(mode)]}`}
      onClick={() => setTheme(cycleTheme(mode))}
      className={cn(
        "inline-flex h-9 w-9 items-center justify-center rounded-full border border-border bg-surface text-heading",
        "transition-colors duration-[var(--duration-fast)] ease-[var(--ease-standard)]",
        "hover:bg-accent focus-visible:outline-none"
      )}
    >
      <Icon className="h-4 w-4" aria-hidden="true" />
      <span className="sr-only">
        {mounted
          ? `${LABELS[mode]} theme (resolved ${resolvedTheme})`
          : "Theme"}
      </span>
    </button>
  );
}

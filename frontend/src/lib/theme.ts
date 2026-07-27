export type ThemeMode = "light" | "dark" | "system";

const ORDER: ThemeMode[] = ["light", "dark", "system"];

export function cycleTheme(current: ThemeMode | undefined): ThemeMode {
  const index = ORDER.indexOf(current ?? "system");
  return ORDER[(index + 1) % ORDER.length];
}

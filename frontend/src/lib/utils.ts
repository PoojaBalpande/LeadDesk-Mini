/**
 * Class name concatenation utility function.
 * Filters out falsy values and joins valid class names into a single string.
 */
export function cn(
  ...classes: (string | undefined | null | false | boolean)[]
): string {
  return classes.filter(Boolean).join(" ");
}

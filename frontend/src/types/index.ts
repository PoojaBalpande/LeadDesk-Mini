import { ElementType, ReactNode } from "react";

/**
 * Common Navigation Item Interface
 */
export interface NavItem {
  label: string;
  href: string;
}

/**
 * Container Component Props
 */
export interface ContainerProps {
  children: ReactNode;
  className?: string;
  as?: ElementType;
}

/**
 * Section Heading Component Props
 */
export interface SectionHeadingProps {
  eyebrow?: string;
  title: string;
  description?: string;
  alignment?: "left" | "center" | "right";
  className?: string;
}

/**
 * Reusable Button Component Props
 */
export interface ButtonProps {
  children: ReactNode;
  variant?: "primary" | "secondary" | "outline";
  size?: "sm" | "md" | "lg";
  type?: "button" | "submit" | "reset";
  disabled?: boolean;
  className?: string;
  href?: string;
  onClick?: () => void;
}

/**
 * Reusable Card Component Props
 */
export interface CardProps {
  title?: string;
  description?: string;
  icon?: ReactNode;
  children?: ReactNode;
  className?: string;
}

/**
 * Reusable Badge Component Props
 */
export interface BadgeProps {
  children: ReactNode;
  variant?: "default" | "outline" | "success";
  className?: string;
}

/**
 * Section Base Props
 */
export interface SectionProps {
  id: string;
  className?: string;
}

/**
 * Surface Component Props
 */
export interface SurfaceProps {
  children: ReactNode;
  variant?: "section" | "surface" | "accent" | "transparent";
  className?: string;
  as?: ElementType;
  hover?: boolean;
}

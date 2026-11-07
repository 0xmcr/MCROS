/**
 * @file next-seo-metadata.tsx
 * @description Production Next.js 14+ Metadata & Open Graph generation template.
 * Includes JSON-LD structured schema for rich Google search results.
 */

import type { Metadata } from "next";

export interface PageSeoConfig {
  title: string;
  description: string;
  path: string;
  ogImage?: string;
}

export function generatePageMetadata(config: PageSeoConfig): Metadata {
  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || "https://mcros.dev";
  const canonicalUrl = `${siteUrl}${config.path}`;
  const defaultOg = `${siteUrl}/api/og?title=${encodeURIComponent(config.title)}`;

  return {
    title: `${config.title} | MCROS`,
    description: config.description,
    alternates: {
      canonical: canonicalUrl,
    },
    openGraph: {
      title: config.title,
      description: config.description,
      url: canonicalUrl,
      siteName: "MCROS",
      images: [
        {
          url: config.ogImage || defaultOg,
          width: 1200,
          height: 630,
          alt: config.title,
        },
      ],
      locale: "en_US",
      type: "website",
    },
    twitter: {
      card: "summary_large_image",
      title: config.title,
      description: config.description,
      images: [config.ogImage || defaultOg],
      creator: "@mcros_official",
    },
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        "max-video-preview": -1,
        "max-image-preview": "large",
        "max-snippet": -1,
      },
    },
  };
}

export function JsonLdOrganization() {
  const schema = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "MCROS",
    "applicationCategory": "DeveloperApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD",
    },
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
    />
  );
}

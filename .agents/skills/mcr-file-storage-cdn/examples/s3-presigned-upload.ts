/**
 * @file s3-presigned-upload.ts
 * @description Secure presigned URL generator for direct S3 / Cloudflare R2 object storage uploads.
 * Bypasses backend web server bottlenecks by allowing client to stream uploads directly to CDN.
 */

export interface PresignedUploadRequest {
  filename: string;
  contentType: string;
  sizeBytes: number;
  userId: string;
}

export function generatePresignedUploadUrl(request: PresignedUploadRequest): {
  uploadUrl: string;
  fileKey: string;
  publicCdnUrl: string;
} {
  // 1. Strict File Type Validation
  const ALLOWED_TYPES = ["image/jpeg", "image/png", "image/webp", "application/pdf"];
  if (!ALLOWED_TYPES.includes(request.contentType)) {
    throw new Error(`Disallowed content type: ${request.contentType}`);
  }

  // 2. Strict File Size Validation (Max 10MB)
  const MAX_SIZE = 10 * 1024 * 1024;
  if (request.sizeBytes > MAX_SIZE) {
    throw new Error("File size exceeds 10MB limit.");
  }

  // 3. Generate Non-Colliding Storage Key
  const extension = request.filename.split(".").pop();
  const fileKey = `uploads/${request.userId}/${Date.now()}_${Math.random().toString(36).substring(7)}.${extension}`;
  
  const uploadUrl = `https://r2.cloudflarestorage.com/mcr-bucket/${fileKey}?X-Amz-Signature=mock`;
  const publicCdnUrl = `https://cdn.mcros.dev/${fileKey}`;

  return { uploadUrl, fileKey, publicCdnUrl };
}

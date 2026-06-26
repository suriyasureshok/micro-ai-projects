import { z } from "zod";

// Define a Zod schema for a ticket object
// Attributes:
// - issue: a string that can be one of the following values: "shipping", "billing", "refund", "technical", or "account"
// - sentiment: a string that can be one of the following values: "positive", "negative", or "neutral"
// - customerName: a string that can be null
export const TicketSchema = z.object({
  issue: z.enum(["shipping", "billing", "refund", "technical", "account"]),
  sentiment: z.enum(["positive", "negative", "neutral"]),
  customerName: z.string().nullable(),
});

export type Ticket = z.infer<typeof TicketSchema>;

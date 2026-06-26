import { generateText, Output } from "ai";
import { google } from "@ai-sdk/google";

import { TicketSchema, type Ticket } from "./schemas";

export async function extractTicket(ticket: string): Promise<Ticket> {
  const result = await generateText({
    model: google("gemini-2.5-flash"),
    output: Output.object({
      schema: TicketSchema,
    }),
    prompt: ticket,
  });
  return result.output;
}

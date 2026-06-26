import express from "express";
import dotenv from "dotenv";

import { extractTicket } from "./ai";

dotenv.config();

const app = express();
app.use(express.json());

app.post("/extract-ticket", async (req, res) => {
  try {
    const ticket = req.body.ticket;
    if (!ticket) {
      return res.status(400).json({ error: "Ticket text is required" });
    }
    const extractedTicket = await extractTicket(ticket);
    res.json(extractedTicket);
  } catch (error) {
    console.error("Error extracting ticket:", error);
    res.status(500).json({ error: "Failed to extract ticket" });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

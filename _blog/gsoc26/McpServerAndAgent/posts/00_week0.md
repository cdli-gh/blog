---
layout: page
title: "MCP Server: Community Bonding"
author: 'Armaan Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'McpServerAndAgent', 'week#0', 'Community Bonding']
---

## Summary

The community bonding period was a good start to GSoC 2026. It kicked off with a joint onboarding session where all four GSoC contributors and their mentors got together. We introduced ourselves, talked a bit about our projects, and got to know the CDLI community. We were also given some baselines to follow around communication and documentation for the rest of the program.

On the technical side, I spent this time finalizing the plan and overall structure for the project. The system has three main parts, the **MCP Server**, the **Chat Interface**, and the **Paper Agent**, and I got a clear picture of how they'll all fit together. The MCP tools were also finalized and confirmed with the mentors.

I had a meeting with my project mentors where I walked them through the architecture and the three components, and we discussed some doubts I had. Those were also posted on Slack to keep things tracked. One interesting decision we made was about the chat interface, whether to build it as a widget or a full separate page. Since the system supports BYOM (Bring Your Own Model), where users plug in their own API keys, going with a dedicated page like `cdli.earth/chat` made more sense. We also agreed to have some free models available by default, so users don't have to bring their own key just to get started.

We also sorted out where the code for each component will live, the MCP Server gets its own repo, while the Chat Interface and Paper Agent will sit inside the existing `cdli/framework` repo.

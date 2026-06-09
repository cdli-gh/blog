---
layout: page
title: Search & Discovery Improvements
author: 'Harsh Chandwani'
tags: ['project', 'gsoc', 'gsoc2026', 'SearchDiscovery', 'search', 'opensearch']
---

## Project Overview

Hi, I'm [Harsh Chandwani](https://www.linkedin.com/in/harsh-chandwani-b9a48238a/), participating in Google Summer of Code 2026 with CDLI. I've been accepted for the project **Search & Discovery Improvements**.

CDLI (Cuneiform Digital Library Initiative) hosts over 340,000 cuneiform artifacts, and search is how most people actually use it. Today that search has three gaps: indexing runs only once nightly (a Logstash full-rebuild of Elasticsearch), so an approved edit can take up to 24 hours to appear; only artifacts go through the search engine, while publications, collections, proveniences, and periods fall back to plain database `LIKE` queries; and Elasticsearch's license conflicts with CDLI's open-source model.

This project fixes all three. It moves to event-driven **incremental indexing** (Transactional Outbox) so approved edits appear in seconds, migrates the backend to **OpenSearch** (Apache 2.0) with a PHP document builder replacing the Logstash Ruby transform, and extends full search to publications, collections, proveniences, and periods.

### Quick Links

| | |
| --- | --- |
| **Student** | [Harsh Chandwani](https://www.linkedin.com/in/harsh-chandwani-b9a48238a/) |
| **Mentors** | [Émilie Pagé-Perron](https://www.linkedin.com/in/epageperron/), [Vedant Wakalkar](https://www.linkedin.com/in/karna98/) |
| **Proposal** | [Search & Discovery Improvements](https://github.com/cdli-gh/Framework/blob/master/Proposal/2026/GSOC-2026-Search%20%26%20Discovery%20Improvements-Proposal.pdf) |
| **GSoC Project** | [GSoC'26](https://summerofcode.withgoogle.com/programs/2026/projects/nrwAEiGp) |
| **Project Idea** | [Ideas List #4.2](https://gitlab.com/cdli/framework/-/wikis/Google-Summer-of-Code-GSoC-2026-Cuneiform-Digital-Library-Initiative-%28CDLI%29-ideas-list#42-search--discovery-improvements--350h) |
| **Contributions** | [Merge Requests](https://gitlab.com/cdli/framework/-/merge_requests?scope=all&state=all&author_username=jinwoo18) |
| **Repository** | [cdli/framework](https://gitlab.com/cdli/framework) |

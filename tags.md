---
title: Tags
layout: tags
---

<main>
{% assign tags =  site.blog | map: 'tags' | join: ','  | split: ',' | uniq %}
{% for tag in tags %}
  <h3>{{ tag }}</h3><br>
  {% for note in site.blog %}
    {% if note.tags contains tag %}
        <a href="{{ site.baseurl }}{{ note.url }}" style="text-decoration:none;">
          <div class="article">
            <p class="a-title">
              {{ note.title }}
            </p>
            <p class="a-author">
              {{ note.url | realtive_url}}
            </p>
          </div>
        </a> 
    {% endif %}
  {% endfor %}
{% endfor %}
</main>


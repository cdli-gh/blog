---
title: Categories
layout: default
---

{% for category in site.categories %}

<h2 id="{{ category[0] | strip }}">{{ category[0] | capitalize }}</h2>
<ul>
	{% for post in category[1] %}
    <li>
		<a class="post_link" href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a>
    </li>
	{% endfor %}
</ul>
{% endfor %}

<style>
    li{
        margin: 10px 0px;
        list-style: none;
    }
    li a{
        text-decoration: none;
    }
</style>

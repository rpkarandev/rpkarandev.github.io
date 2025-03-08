---
title: Publications
layout: default
#permalink: /publications

listing:
  contents: publications/
  type: grid
  sort: year
  categories: true
  filter-ui: true
  image-placeholder: /images/samico.png
---

<section class="box-content" style="width:100%">
<div class="publication-wrapper" style="text-align: justify;text-justify: inter-word;">
  <h2>List of Publications</h2>
  <hr><br>

  {% assign pub_list = site.data.publications | sort: "Year" | reverse %}

  <ol>
    {% for citation in pub_list %}
      {% assign authors = citation.Authors | split: ";" %}
      {% assign formatted_authors = "" %}

      {% for author in authors %}
        {% assign author_trimmed = author | strip %}
        {% if author_trimmed contains "Prabakaran" %}
          {% assign formatted_authors = formatted_authors | append: "<strong>" | append: author_trimmed | append: "</strong>" %}
        {% else %}
          {% assign formatted_authors = formatted_authors | append: author_trimmed %}
        {% endif %}

        {% unless forloop.last %}
          {% assign formatted_authors = formatted_authors | append: ", " %}
        {% endunless %}
      {% endfor %}

      {% assign journal = citation.Publication %}
      {% assign highlighted_journal = "<em><strong>" | append: journal | append: "</strong></em>" %}

      <li>
        {{ formatted_authors }} ({{ citation.Year }})"{{ citation.Title }}."
        {{ highlighted_journal }}.
        {%if citation.Volume and citation.Volume != "" %}, {{citation.Volume}}{% if citation.Number %}({{citation.Number}}){%endif%}{% endif %} 
        {%if citation.Pages %}:{{citation.Pages}}{% endif %}
      </li>

    {% endfor %}
  </ol>
</div>
</section>

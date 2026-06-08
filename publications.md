---
title: Publications
nav_id: publications
permalink: /publications/
layout: default
description: Peer-reviewed publications and preprints by R. Prabakaran in computational biology, machine learning, and protein bioinformatics.
---

{% assign s = site.data.scholar %}
{% if site.show_citations and s and s.total_citations and s.total_citations > 0 %}
<section class="box-content" style="width:100%">
  <h2>Citation metrics</h2>
  <hr>
  <div class="scholar-stats">
    <div class="scholar-stat"><span class="num">{{ s.total_citations }}</span><span class="lbl">Citations</span></div>
    <div class="scholar-stat"><span class="num">{{ s.h_index }}</span><span class="lbl">h-index</span></div>
    <div class="scholar-stat"><span class="num">{{ s.i10_index }}</span><span class="lbl">i10-index</span></div>
  </div>
  {% if s.citations_per_year and s.citations_per_year != empty %}
    {% assign maxc = 1 %}
    {% for pair in s.citations_per_year %}{% if pair[1] > maxc %}{% assign maxc = pair[1] %}{% endif %}{% endfor %}
    <div class="cite-graph" aria-label="Citations per year">
      {% for pair in s.citations_per_year %}
        {% assign h = pair[1] | times: 100 | divided_by: maxc %}
        <div class="bar-col">
          <span class="bar-val">{{ pair[1] }}</span>
          <div class="bar" style="height: {{ h }}%;"></div>
          <span class="bar-yr">{{ pair[0] }}</span>
        </div>
      {% endfor %}
    </div>
  {% endif %}
  <p class="scholar-updated">Source: Google Scholar{% if s.updated and s.updated != "" %}, updated {{ s.updated }}{% endif %}. <a class="pub-link" href="https://scholar.google.com/citations?user=7aAKswUAAAAJ&hl=en" target="_blank" rel="noopener">View profile&nbsp;&#8599;</a></p>
</section>
{% endif %}

<section class="box-content" style="width:100%">
<div class="publication-wrapper" style="text-align: justify;text-justify: inter-word;">

  <p class="pub-legend" style="font-size:0.85em;color:#666;">* corresponding author. <strong>Bold</strong> = R. Prabakaran.</p>

  {% assign selected = site.data.publications | where: "selected", true | sort: "Year" | reverse %}
  {% if selected.size > 0 %}
  <h2>&#9733; Selected publications</h2>
  <hr><br>
  <ol>
    {% for citation in selected %}{% include pub-item.html citation=citation %}{% endfor %}
  </ol>
  <br>
  {% endif %}

  <h2>All publications</h2>
  <hr><br>
  {% assign pub_list = site.data.publications | sort: "Year" | reverse %}
  <ol>
    {% for citation in pub_list %}{% include pub-item.html citation=citation %}{% endfor %}
  </ol>
</div>
</section>

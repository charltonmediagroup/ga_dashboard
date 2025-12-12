# Introduction
This Contains static elements for Dasboard
Latest News ticker: `index.html`
Exclusives ticket: `ticket.html`
1 large video with title: `vimeo.html`

# Parameters
This is the list of parameters and each property that is used in the pages
## index.html - Latest News Ticker


### `code`

* **Type:** `string`
* **Description:** Refer on which website it gets the data, field in `data.json`
* **Options:** `sbr, hkb, abf, ia, ra, hca, ap, qsr, qsr-asia, qsr-au, qsr-uk`
* **Default:** `"sbr"`

---

### `theme-color`

* **Type:** `string`
* **Description:** Option if the color in `data.json` is applied to the element
* **Options:** `true, 1, True, TRUE`
* **Default:** `"false"`

---
### `speed`

* **Type:** `int`
* **Description:** Speed of headline animation in px per second
* **Options:** >0
* **Default:** 200

---
---
---

## ticket.html - Exclusive News


### `code`

* **Type:** `string`
* **Description:** Refer on which website it gets the data, field in `data.json`
* **Options:** `sbr, hkb, abf, ia, ra, hca, ap, qsr, qsr-asia, qsr-au, qsr-uk`
* **Default:** `"sbr"`

---

### `theme-color`

* **Type:** `string`
* **Description:** Option if the color in `data.json` is applied to the element
* **Options:** `true, 1, True, TRUE`
* **Default:** `"false"`

---
### `duration`

* **Type:** `int`
* **Description:** Duration of headline showing in millisecond
* **Options:** >0
* **Default:** 4000

---
---
---
## ticket.html - Exclusive News


### `code`

* **Type:** `string`
* **Description:** Refer on which website it gets the data, field in `data.json`
* **Options:** `sbr, hkb, abf, ia, ra, hca, ap, qsr, qsr-asia, qsr-au, qsr-uk`
* **Default:** `"sbr"`

---
### `duration`

* **Type:** `int`
* **Description:** Duration of eac video being played
* **Options:** >0
* **Default:** 30

---
### `start`

* **Type:** `int`
* **Description:** index of the video in the RSS to be played first
* **Options:** >0
* **Default:** 1
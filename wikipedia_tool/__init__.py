import requests

WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"


def search_page(query):
    params = {"action": "query", "list": "search", "srsearch": query, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    search_results = [result["title"] for result in data["query"]["search"]]
    return search_results


def get_summary(title):
    params = {
        "action": "query",
        "prop": "extracts",
        "titles": title,
        "explaintext": True,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    page_summary = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "extract"
    ]
    return page_summary


def get_page_content(title):
    params = {"action": "parse", "page": title, "prop": "wikitext", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    page_content = data["parse"]["wikitext"]["*"]
    return page_content


def get_page_links(title):
    params = {"action": "query", "prop": "links", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    links = [
        link["title"]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "links", []
        )
    ]
    return links


def get_page_images(title):
    params = {"action": "query", "prop": "images", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    images = [
        image["title"]
        for image in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "images", []
        )
    ]
    return images


def get_page_categories(title):
    params = {
        "action": "query",
        "prop": "categories",
        "titles": title,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    categories = [
        category["title"]
        for category in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("categories", [])
    ]
    return categories


def random_page():
    params = {
        "action": "query",
        "generator": "random",
        "grnnamespace": 0,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    random_page = list(data["query"]["pages"].values())[0]["title"]
    return random_page


def get_page_sections(title):
    params = {"action": "parse", "page": title, "prop": "sections", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sections = [section["line"] for section in data["parse"]["sections"]]
    return sections


def get_page_references(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "externallinks",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    references = data["parse"]["externallinks"]
    return references


def get_page_languages(title):
    params = {"action": "query", "prop": "langlinks", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages = [
        langlink["lang"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages


def get_page_coordinates(title):
    params = {
        "action": "query",
        "prop": "coordinates",
        "titles": title,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    coordinates = data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
        "coordinates", []
    )
    return coordinates


def get_page_info(title):
    params = {"action": "query", "prop": "info", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    page_info = data["query"]["pages"][list(data["query"]["pages"].keys())[0]]
    return page_info


def get_page_history(title):
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvlimit": 10,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    revisions = data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
        "revisions", []
    )
    return revisions


def get_page_editors(title):
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvdir": "newer",
        "rvlimit": 1,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    editor = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0].get("user", "")
    return editor


def get_page_contributors(title):
    params = {
        "action": "query",
        "prop": "contributors",
        "titles": title,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    contributors = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "contributors"
    ]
    return contributors


def get_page_statistics(title):
    params = {"action": "query", "prop": "pageprops", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    page_statistics = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ].get("pageprops", {})
    return page_statistics


def get_page_backlinks(title):
    params = {
        "action": "query",
        "list": "backlinks",
        "bltitle": title,
        "bllimit": 10,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    backlinks = [link["title"] for link in data["query"]["backlinks"]]
    return backlinks


def get_page_templates(title):
    params = {"action": "query", "prop": "templates", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    templates = [
        template["title"]
        for template in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("templates", [])
    ]
    return templates


def get_page_external_links(title):
    params = {"action": "query", "prop": "extlinks", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    external_links = [
        link["*"]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return external_links


def get_page_toc(title):
    params = {"action": "parse", "page": title, "prop": "sections", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    toc = [
        {"level": section["toclevel"], "title": section["line"]}
        for section in data["parse"]["sections"]
    ]
    return toc


def get_page_infobox(title):
    params = {"action": "parse", "page": title, "prop": "infobox", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    infobox = data["parse"].get("infobox", {})
    return infobox


def get_page_metadata(title):
    params = {"action": "query", "prop": "pageprops", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    page_metadata = data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
        "pageprops", {}
    )
    return page_metadata


def get_page_references(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "externallinks",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    references = data["parse"]["externallinks"]
    return references


def get_page_citations(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "text",
        "section": 0,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    citations = data["parse"]["text"]["*"]
    return citations


def get_page_table_of_contents(title):
    params = {"action": "parse", "page": title, "prop": "sections", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    toc = [
        {"level": section["toclevel"], "title": section["line"]}
        for section in data["parse"]["sections"]
    ]
    return toc


def get_page_content_length(title):
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvprop": "size",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    page_id = list(data["query"]["pages"].keys())[0]
    content_length = data["query"]["pages"][page_id]["revisions"][0]["size"]
    return content_length


def get_page_revision(title):
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvlimit": 1,
        "rvprop": "user|comment|timestamp",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    revision_info = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]
    return revision_info


def get_page_discussion(title):
    params = {
        "action": "query",
        "prop": "discussion",
        "titles": title,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    discussion = data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
        "discussion", []
    )
    return discussion


def get_page_translation(title):
    params = {"action": "query", "prop": "langlinks", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    translations = [
        langlink["lang"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return translations


def get_page_versions(title):
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": title,
        "rvlimit": 10,
        "rvprop": "user|timestamp",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    versions = [
        {"user": rev["user"], "timestamp": rev["timestamp"]}
        for rev in data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
            "revisions"
        ]
    ]
    return versions


def get_page_similarity(title):
    params = {"action": "morelike", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    similarity = data["morelike"]["docs"]
    return similarity


def get_page_related(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "links",
        "pllimit": 10,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    related_pages = [
        link["title"]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "links", []
        )
    ]
    return related_pages


def get_page_suggestions(title):
    params = {"action": "opensearch", "search": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    suggestions = response.json()[1]
    return suggestions


def get_page_related_topics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "categories",
        "clshow": "!hidden",
        "cllimit": 10,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    related_topics = [
        category["title"]
        for category in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("categories", [])
    ]
    return related_topics


def get_page_audio(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "videoinfo|images",
        "viprop": "url|size",
        "viextparam": "url",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    audio_info = [
        item["url"]
        for item in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "videoinfo", []
        )
    ]
    return audio_info


def get_page_video(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "videoinfo",
        "viprop": "url|size",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    video_info = [
        item["url"]
        for item in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "videoinfo", []
        )
    ]
    return video_info


def get_page_references_count(title):
    params = {"action": "query", "prop": "extlinks", "titles": title, "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    references_count = len(
        data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    )
    return references_count


def get_page_references_list(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "externallinks",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    references_list = data["parse"]["externallinks"]
    return references_list


def get_page_references_sections(title):
    params = {"action": "parse", "page": title, "prop": "sections", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    references_sections = [section["line"] for section in data["parse"]["sections"]]
    return references_sections


def get_page_references_sources(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "externallinks",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    references_sources = [source["*"] for source in data["parse"]["externallinks"]]
    return references_sources


def get_page_references_info(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 0,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    references_info = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return references_info


def get_page_references_authors(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "user",
        "rvlimit": 10,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    authors = [
        rev["user"]
        for rev in data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
            "revisions"
        ]
    ]
    return authors


def get_page_references_dates(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "timestamp",
        "rvlimit": 10,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    dates = [
        rev["timestamp"]
        for rev in data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
            "revisions"
        ]
    ]
    return dates


def get_page_references_topics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "categories",
        "clshow": "!hidden",
        "cllimit": 10,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    topics = [
        category["title"]
        for category in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("categories", [])
    ]
    return topics


def get_page_references_categories(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "categories",
        "clshow": "!hidden",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    categories = [
        category["title"]
        for category in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("categories", [])
    ]
    return categories


def get_page_references_formats(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "externallinks",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    references_formats = [
        link.split(".")[-1] for link in data["parse"]["externallinks"]
    ]
    return references_formats


def get_page_references_links(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "externallinks",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    references_links = data["parse"]["externallinks"]
    return references_links


def get_page_references_citations(title):
    params = {"action": "parse", "page": title, "prop": "sections", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    citations = [
        section["line"]
        for section in data["parse"]["sections"]
        if "Citations" in section["line"]
    ]
    return citations


def get_page_references_resources(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    resources = [
        link["*"]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return resources


def get_page_references_sources_info(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "externallinks",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_info = [
        {"title": link["*"], "url": link["url"]}
        for link in data["parse"]["externallinks"]
    ]
    return sources_info


def get_page_references_sources_authors(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_authors = [
        link["*"].split("/")[2]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_authors


def get_page_references_sources_dates(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_dates = [
        link["*"].split("/")[4]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_dates


def get_page_references_sources_topics(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_topics = [
        link["*"].split("/")[3]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_topics


def get_page_references_sources_categories(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_categories = [
        link["*"].split("/")[1]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_categories


def get_page_references_sources_formats(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_formats = [
        link["*"].split(".")[-1]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_formats


def get_page_references_sources_links(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_links = [
        link["*"]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_links


def get_page_references_sources_citations(title):
    params = {"action": "parse", "page": title, "prop": "sections", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_citations = [
        section["line"]
        for section in data["parse"]["sections"]
        if "Citations" in section["line"]
    ]
    return sources_citations


def get_page_references_sources_resources(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_resources = [
        link["*"]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_resources


def get_page_references_sources_info(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "externallinks",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_info = [
        {"title": link["*"], "url": link["url"]}
        for link in data["parse"]["externallinks"]
    ]
    return sources_info


def get_page_references_sources_authors(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_authors = [
        link["*"].split("/")[2]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_authors


def get_page_references_sources_dates(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_dates = [
        link["*"].split("/")[4]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_dates


def get_page_references_sources_topics(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_topics = [
        link["*"].split("/")[3]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_topics


def get_page_references_sources_categories(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_categories = [
        link["*"].split("/")[1]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_categories


def get_page_references_sources_formats(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_formats = [
        link["*"].split(".")[-1]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_formats


def get_page_references_sources_links(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_links = [
        link["*"]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_links


def get_page_references_sources_citations(title):
    params = {"action": "parse", "page": title, "prop": "sections", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_citations = [
        section["line"]
        for section in data["parse"]["sections"]
        if "Citations" in section["line"]
    ]
    return sources_citations


def get_page_references_sources_resources(title):
    params = {"action": "query", "titles": title, "prop": "extlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sources_resources = [
        link["*"]
        for link in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "extlinks", []
        )
    ]
    return sources_resources


def get_page_disambiguation(title):
    params = {
        "action": "query",
        "titles": title,
        "redirects": "true",
        "prop": "revisions",
        "rvprop": "content",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    if "pages" in data:
        page_id = list(data["query"]["pages"].keys())[0]
        content = data["query"]["pages"][page_id]["revisions"][0]["*"]
        if "{{disambiguation" in content.lower():
            return True
    return False


def get_page_redirects(title):
    params = {"action": "query", "titles": title, "redirects": "true", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    redirects = [redirect["to"] for redirect in data["query"]["redirects"]]
    return redirects


def get_page_translations(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    translations = [
        langlink["*"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return translations


def get_page_languages_list(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages_list = [
        langlink["lang"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages_list


def get_page_languages_codes(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages_codes = [
        langlink["lang"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages_codes


def get_page_languages_info(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages_info = [
        {"lang": langlink["lang"], "title": langlink["*"]}
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages_info


def get_page_languages_regions(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages_regions = [
        langlink["*"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages_regions


def get_page_languages_speakers(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages_speakers = [
        langlink["*"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages_speakers


def get_page_languages_family(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages_family = [
        langlink["*"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages_family


def get_page_languages_scripts(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages_scripts = [
        langlink["*"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages_scripts


def get_page_languages_variants(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages_variants = [
        langlink["*"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages_variants


def get_page_languages_dialects(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages_dialects = [
        langlink["*"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages_dialects


def get_page_languages_translations(title):
    params = {"action": "query", "titles": title, "prop": "langlinks", "format": "json"}
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    languages_translations = [
        langlink["*"]
        for langlink in data["query"]["pages"][
            list(data["query"]["pages"].keys())[0]
        ].get("langlinks", [])
    ]
    return languages_translations


def get_page_languages_pronunciations(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "pronunciations",
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    pronunciations = [
        pron["*"]
        for pron in data["query"]["pages"][list(data["query"]["pages"].keys())[0]].get(
            "pronunciation", []
        )
    ]
    return pronunciations


def get_page_languages_learn(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 0,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    learn_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return learn_text


def get_page_languages_teach(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 1,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    teach_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return teach_text


def get_page_languages_speak(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 2,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    speak_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return speak_text


def get_page_languages_write(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 3,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    write_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return write_text


def get_page_languages_read(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 4,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    read_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return read_text


def get_page_languages_understand(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 5,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    understand_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return understand_text


def get_page_languages_grammar(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 6,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    grammar_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return grammar_text


def get_page_languages_vocabulary(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 7,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    vocabulary_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return vocabulary_text


def get_page_languages_alphabet(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 8,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    alphabet_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return alphabet_text


def get_page_languages_words(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 9,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    words_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return words_text


def get_page_languages_meanings(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 10,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    meanings_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return meanings_text


def get_page_languages_synonyms(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 11,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    synonyms_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return synonyms_text


def get_page_languages_antonyms(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 12,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    antonyms_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return antonyms_text


def get_page_languages_history(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 13,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    history_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return history_text


def get_page_languages_evolution(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 14,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    evolution_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return evolution_text


def get_page_languages_origin(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 15,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    origin_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return origin_text


def get_page_languages_spread(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 16,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    spread_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return spread_text


def get_page_languages_decline(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 17,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    decline_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return decline_text


def get_page_languages_revival(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 18,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    revival_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return revival_text


def get_page_languages_influence(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 19,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    influence_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return influence_text


def get_page_languages_impact(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 20,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    impact_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return impact_text


def get_page_languages_usage(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 21,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    usage_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return usage_text


def get_page_languages_literature(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 22,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    literature_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return literature_text


def get_page_languages_songs(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 23,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    songs_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return songs_text


def get_page_languages_poetry(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 24,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    poetry_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return poetry_text


def get_page_languages_proverbs(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 25,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    proverbs_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return proverbs_text


def get_page_languages_quotes(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 26,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    quotes_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return quotes_text


def get_page_languages_books(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 27,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    books_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return books_text


def get_page_languages_writing(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 28,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    writing_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return writing_text


def get_page_languages_phonetics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 29,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    phonetics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return phonetics_text


def get_page_languages_syllables(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 30,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    syllables_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return syllables_text


def get_page_languages_pronouns(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 31,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    pronouns_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return pronouns_text


def get_page_languages_verbs(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 32,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    verbs_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return verbs_text


def get_page_languages_nouns(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 33,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    nouns_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return nouns_text


def get_page_languages_adjectives(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 34,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    adjectives_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return adjectives_text


def get_page_languages_adverbs(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 35,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    adverbs_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return adverbs_text


def get_page_languages_prepositions(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 36,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    prepositions_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return prepositions_text


def get_page_languages_conjunctions(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 37,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    conjunctions_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return conjunctions_text


def get_page_languages_interjections(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 38,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    interjections_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return interjections_text


def get_page_languages_participles(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 39,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    participles_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return participles_text


def get_page_languages_articles(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 40,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    articles_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return articles_text


def get_page_languages_numbers(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 41,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    numbers_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return numbers_text


def get_page_languages_plural(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 42,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    plural_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return plural_text


def get_page_languages_singular(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 43,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    singular_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return singular_text


def get_page_languages_gender(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 44,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    gender_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return gender_text


def get_page_languages_cases(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 45,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    cases_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return cases_text


def get_page_languages_tenses(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 46,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    tenses_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return tenses_text


def get_page_languages_aspects(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 47,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    aspects_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return aspects_text


def get_page_languages_moods(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 48,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    moods_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return moods_text


def get_page_languages_voice(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 49,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    voice_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return voice_text


def get_page_languages_punctuation(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 50,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    punctuation_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return punctuation_text


def get_page_languages_spacing(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 51,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    spacing_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return spacing_text


def get_page_languages_capitalization(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 52,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    capitalization_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return capitalization_text


def get_page_languages_orthography(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 53,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    orthography_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return orthography_text


def get_page_languages_dictionaries(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 54,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    dictionaries_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return dictionaries_text


def get_page_languages_grammar_rules(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 55,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    grammar_rules_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return grammar_rules_text


def get_page_languages_accent(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 56,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    accent_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return accent_text


def get_page_languages_intonation(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 57,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    intonation_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return intonation_text


def get_page_languages_dialectology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 58,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    dialectology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return dialectology_text


def get_page_languages_philology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 59,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    philology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return philology_text


def get_page_languages_linguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 60,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    linguistics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return linguistics_text


def get_page_languages_semantics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 61,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    semantics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return semantics_text


def get_page_languages_pragmatics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 62,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    pragmatics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return pragmatics_text


def get_page_languages_syntax(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 63,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    syntax_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return syntax_text


def get_page_languages_lexicography(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 64,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    lexicography_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return lexicography_text


def get_page_languages_etymology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 65,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    etymology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return etymology_text


def get_page_languages_paleography(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 66,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    paleography_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return paleography_text


def get_page_languages_graphemics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 67,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    graphemics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return graphemics_text


def get_page_languages_phonology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 68,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    phonology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return phonology_text


def get_page_languages_morphology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 69,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    morphology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return morphology_text


def get_page_languages_sociolinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 70,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sociolinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return sociolinguistics_text


def get_page_languages_psycholinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 71,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    psycholinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return psycholinguistics_text


def get_page_languages_neurolinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 72,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    neurolinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return neurolinguistics_text


def get_page_languages_computational_linguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 73,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    computational_linguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return computational_linguistics_text


def get_page_languages_corpus_linguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 74,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    corpus_linguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return corpus_linguistics_text


def get_page_languages_descriptive_linguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 75,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    descriptive_linguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return descriptive_linguistics_text


def get_page_languages_historical_linguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 76,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    historical_linguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return historical_linguistics_text


def get_page_languages_mathematical_linguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 77,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    mathematical_linguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return mathematical_linguistics_text


def get_page_languages_medical_linguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 78,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    medical_linguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return medical_linguistics_text


def get_page_languages_philosophy_of_language(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 79,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    philosophy_of_language_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return philosophy_of_language_text


def get_page_languages_phonetics_and_phonology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 80,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    phonetics_and_phonology_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return phonetics_and_phonology_text


def get_page_languages_psycholinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 81,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    psycholinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return psycholinguistics_text


def get_page_languages_sociolinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 82,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sociolinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return sociolinguistics_text


def get_page_languages_stylistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 83,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    stylistics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return stylistics_text


def get_page_languages_text_linguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 84,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    text_linguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return text_linguistics_text


def get_page_languages_typology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 85,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    typology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return typology_text


def get_page_languages_kinship_terms(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 86,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    kinship_terms_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return kinship_terms_text


def get_page_languages_color_terms(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 87,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    color_terms_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return color_terms_text


def get_page_languages_animal_sounds(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 88,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    animal_sounds_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return animal_sounds_text


def get_page_languages_ethnolinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 89,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    ethnolinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return ethnolinguistics_text


def get_page_languages_language_and_gender(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 90,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_and_gender_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_and_gender_text


def get_page_languages_language_and_age(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 91,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_and_age_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_and_age_text


def get_page_languages_language_and_identity(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 92,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_and_identity_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_and_identity_text


def get_page_languages_language_and_power(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 93,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_and_power_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_and_power_text


def get_page_languages_language_and_society(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 94,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_and_society_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_and_society_text


def get_page_languages_language_and_culture(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 95,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_and_culture_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_and_culture_text


def get_page_languages_language_contact(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 96,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_contact_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_contact_text


def get_page_languages_language_change(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 97,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_change_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_change_text


def get_page_languages_language_development(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 98,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_development_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_development_text


def get_page_languages_language_endangerment(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 99,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_endangerment_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_endangerment_text


def get_page_languages_language_extinction(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 100,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_extinction_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_extinction_text


def get_page_languages_language_policy(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 101,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_policy_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_policy_text


def get_page_languages_language_technology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 102,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_technology_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_technology_text


def get_page_languages_language_universals(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 103,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_universals_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_universals_text


def get_page_languages_language_varieties(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 104,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_varieties_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_varieties_text


def get_page_languages_language_vitality(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 105,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_vitality_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_vitality_text


def get_page_languages_language_engineering(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 106,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_engineering_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_engineering_text


def get_page_languages_language_processing(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 107,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_processing_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_processing_text


def get_page_languages_philology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 108,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    philology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return philology_text


def get_page_languages_phonetics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 109,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    phonetics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return phonetics_text


def get_page_languages_phonology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 110,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    phonology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return phonology_text


def get_page_languages_pragmatics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 111,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    pragmatics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return pragmatics_text


def get_page_languages_prosody(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 112,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    prosody_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return prosody_text


def get_page_languages_psycholinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 113,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    psycholinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return psycholinguistics_text


def get_page_languages_reading(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 114,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    reading_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return reading_text


def get_page_languages_writing(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 115,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    writing_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return writing_text


def get_page_languages_listening(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 116,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    listening_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return listening_text


def get_page_languages_speaking(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 117,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    speaking_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return speaking_text


def get_page_languages_vocabulary(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 118,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    vocabulary_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return vocabulary_text


def get_page_languages_grammar(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 119,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    grammar_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return grammar_text


def get_page_languages_pronunciation(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 120,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    pronunciation_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return pronunciation_text


def get_page_languages_comprehension(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 121,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    comprehension_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return comprehension_text


def get_page_languages_conversation(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 122,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    conversation_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return conversation_text


def get_page_languages_translation(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 123,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    translation_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return translation_text


def get_page_languages_literature(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 124,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    literature_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return literature_text


def get_page_languages_culture(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 125,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    culture_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return culture_text


def get_page_languages_history(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 126,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    history_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return history_text


def get_page_languages_geography(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 127,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    geography_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return geography_text


def get_page_languages_philosophy(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 128,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    philosophy_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return philosophy_text


def get_page_languages_religion(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 129,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    religion_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return religion_text


def get_page_languages_mythology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 130,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    mythology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return mythology_text


def get_page_languages_art(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 131,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    art_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return art_text


def get_page_languages_music(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 132,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    music_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return music_text


def get_page_languages_sports(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 133,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sports_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return sports_text


def get_page_languages_science(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 134,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    science_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return science_text


def get_page_languages_technology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 135,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    technology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return technology_text


def get_page_languages_economy(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 136,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    economy_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return economy_text


def get_page_languages_politics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 137,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    politics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return politics_text


def get_page_languages_society(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 138,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    society_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return society_text


def get_page_languages_education(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 139,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    education_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return education_text


def get_page_languages_health(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 140,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    health_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return health_text


def get_page_languages_environment(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 141,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    environment_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return environment_text


def get_page_languages_architecture(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 142,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    architecture_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return architecture_text


def get_page_languages_cuisine(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 143,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    cuisine_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return cuisine_text


def get_page_languages_fashion(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 144,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    fashion_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return fashion_text


def get_page_languages_law(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 145,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    law_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return law_text


def get_page_languages_military(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 146,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    military_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return military_text


def get_page_languages_media(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 147,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    media_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return media_text


def get_page_languages_entertainment(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 148,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    entertainment_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return entertainment_text


def get_page_languages_linguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 0,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    linguistics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return linguistics_text


def get_page_languages_phonetics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 1,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    phonetics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return phonetics_text


def get_page_languages_morphology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 2,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    morphology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return morphology_text


def get_page_languages_syntax(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 3,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    syntax_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return syntax_text


def get_page_languages_semantics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 4,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    semantics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return semantics_text


def get_page_languages_pragmatics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 5,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    pragmatics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return pragmatics_text


def get_page_languages_lexicography(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 6,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    lexicography_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return lexicography_text


def get_page_languages_stylistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 7,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    stylistics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return stylistics_text


def get_page_languages_dialectology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 8,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    dialectology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return dialectology_text


def get_page_languages_sociolinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 9,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sociolinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return sociolinguistics_text


def get_page_languages_psycholinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 10,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    psycholinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return psycholinguistics_text


def get_page_languages_neurolinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 11,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    neurolinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return neurolinguistics_text


def get_page_languages_evolution(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 12,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    evolution_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return evolution_text


def get_page_languages_diversity(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 13,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    diversity_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return diversity_text


def get_page_languages_change(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 14,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    change_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return change_text


def get_page_languages_classification(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 15,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    classification_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return classification_text


def get_page_languages_reconstruction(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 16,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    reconstruction_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return reconstruction_text


def get_page_languages_description(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 17,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    description_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return description_text


def get_page_languages_comparison(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 18,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    comparison_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return comparison_text


def get_page_languages_relationship(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 19,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    relationship_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return relationship_text


def get_page_languages_variation(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 20,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    variation_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return variation_text


def get_page_languages_contact(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 21,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    contact_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return contact_text


def get_page_languages_influence(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 22,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    influence_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return influence_text


def get_page_languages_isolation(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 23,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    isolation_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return isolation_text


def get_page_languages_migration(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 24,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    migration_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return migration_text


def get_page_languages_adaptation(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 25,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    adaptation_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return adaptation_text


def get_page_languages_borrowing(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 26,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    borrowing_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return borrowing_text


def get_page_languages_creole(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 27,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    creole_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return creole_text


def get_page_languages_pidgin(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 28,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    pidgin_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return pidgin_text


def get_page_languages_globalization(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 29,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    globalization_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return globalization_text


def get_page_languages_standardization(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 30,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    standardization_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return standardization_text


def get_page_languages_preservation(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 31,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    preservation_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return preservation_text


def get_page_languages_revitalization(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 32,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    revitalization_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return revitalization_text


def get_page_languages_policy(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 33,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    policy_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return policy_text


def get_page_languages_rights(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 34,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    rights_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return rights_text


def get_page_languages_documentation(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 35,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    documentation_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return documentation_text


def get_page_languages_orthography(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 36,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    orthography_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return orthography_text


def get_page_languages_lexicography(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 37,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    lexicography_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return lexicography_text


def get_page_languages_grammatics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 38,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    grammatics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return grammatics_text


def get_page_languages_phonology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 39,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    phonology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return phonology_text


def get_page_languages_morphology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 40,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    morphology_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return morphology_text


def get_page_languages_pragmatics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 41,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    pragmatics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return pragmatics_text


def get_page_languages_semantics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 42,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    semantics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return semantics_text


def get_page_languages_stylistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 43,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    stylistics_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return stylistics_text


def get_page_languages_sociolinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 44,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sociolinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return sociolinguistics_text


def get_page_languages_psycholinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 45,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    psycholinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return psycholinguistics_text


def get_page_languages_neurolinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 46,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    neurolinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return neurolinguistics_text


def get_page_languages_computational(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 47,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    computational_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return computational_text


def get_page_languages_corpus(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 48,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    corpus_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return corpus_text


def get_page_languages_descriptive(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 49,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    descriptive_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return descriptive_text


def get_page_languages_historical(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 50,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    historical_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return historical_text


def get_page_languages_applied(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 51,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    applied_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return applied_text


def get_page_languages_forensic(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 52,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    forensic_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return forensic_text


def get_page_languages_educational(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 53,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    educational_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return educational_text


def get_page_languages_clinical(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 54,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    clinical_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return clinical_text


def get_page_languages_cognitive(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 55,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    cognitive_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return cognitive_text


def get_page_languages_developmental(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 56,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    developmental_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return developmental_text


def get_page_languages_evolutionary(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 57,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    evolutionary_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return evolutionary_text


def get_page_languages_experimental(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 58,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    experimental_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return experimental_text


def get_page_languages_discourse(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 59,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    discourse_text = data["query"]["pages"][list(data["query"]["pages"].keys())[0]][
        "revisions"
    ][0]["*"]
    return discourse_text


def get_page_languages_phonetics_and_phonology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 60,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    phonetics_phonology_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return phonetics_phonology_text


def get_page_languages_semantics_and_pragmatics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 61,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    semantics_pragmatics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return semantics_pragmatics_text


def get_page_languages_sociolinguistics_and_psycholinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 62,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    sociolinguistics_psycholinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return sociolinguistics_psycholinguistics_text


def get_page_languages_linguistic_theories(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 63,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    linguistic_theories_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return linguistic_theories_text


def get_page_languages_language_technology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 64,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    language_technology_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return language_technology_text


def get_page_languages_corpus_linguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 65,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    corpus_linguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return corpus_linguistics_text


def get_page_languages_ethnolinguistics(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 66,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    ethnolinguistics_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return ethnolinguistics_text


def get_page_languages_linguistic_anthropology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 67,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    linguistic_anthropology_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return linguistic_anthropology_text


def get_page_languages_linguistic_typology(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 68,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    linguistic_typology_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return linguistic_typology_text


def get_page_languages_linguistic_universals(title):
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": 69,
        "format": "json",
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    linguistic_universals_text = data["query"]["pages"][
        list(data["query"]["pages"].keys())[0]
    ]["revisions"][0]["*"]
    return linguistic_universals_text

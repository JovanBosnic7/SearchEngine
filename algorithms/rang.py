def rang(graph, trie, result, words):
    rang_result = {}

    for html in result:
        dolazeci = graph.odlazeci[html]
        number_links = len(dolazeci)
        number_words_in_links = 0
        for link in dolazeci:
            if link in result:
                for word in words:
                    try:
                        number_words_in_links += trie.get_counters(word)[link]
                    except KeyError:
                        continue

        number_words = 0
        for word in words:
            try:
                number_words += trie.get_counters(word)[html]
            except KeyError:
                continue

        rang_result[html] = int(number_words + number_links * 0.7 + number_words_in_links * 0.5)

    return rang_result
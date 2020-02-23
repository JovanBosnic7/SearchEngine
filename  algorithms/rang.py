def rang(graph, result):
    rang_result={}

    for html in result.keys():
        dolazeci= graph.odlazeci_html(html)
        number_links= len(dolazeci)
        number_words_in_links=0
        for link in dolazeci:
            if link in result.keys():
                number_words_in_links += result[link]

        rang_result[html] = int (result[html] + number_links * 0.7 + number_words_in_links * 0.5)


    return rang_result

if __name__ == '__main__':
    with open('orig.txt', 'r',encoding="utf-8") as x, open('orig_0.8_rep.txt', 'r',encoding="utf-8") as y:
        content_x = x.read()
        content_y = y.read()
        similarity = MinHashSimilarity(content_x, content_y)
        similarity = similarity.main()
        print('相似度: %.2f%%' % (similarity*100))
    m = [
        [3, 1, 0, 2],
        [3, 0, 1, 2],
        [3, 1, 2, 0],
        [0, 3, 2, 1]
    ]

    w = [
            [3, 0, 2, 1],
            [3, 1, 2, 0],
            [0, 1, 3, 2],
            [3, 0, 2, 1]
        ]
    algo = GayleShapely(m, w, trace = False)

    algo.match()

    assert algo.get_matches() == [3, 1, 2, 0]
    main()
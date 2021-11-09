verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2


def bereken_maandkosten(km_per_maand) -> float:
    return round((km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand, 2)


if __name__ == "__main__":
    while True:
        resp = input("Hoeveel kilometer rij je per maand? ")
        try:
            float(resp)
        except ValueError:
            print(f"{resp} is geen geldig getal!")
            continue
        print(f"Je maand kosten zijn: €{bereken_maandkosten(float(resp))}")



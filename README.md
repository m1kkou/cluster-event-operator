Tämä on opinnäytetyön PoC projekti. Projektin tavoitteena on lisätä näkyvyyttä Kubernetes klusteriin hyödyntämällä Operator-kaavaa.

Prosessi:

1. Uusi deployment luodaan -operaattori-> luo uusi CRD: DeployEvent
2. Deployment resurssia päivitetään -operaattori-> päivitä CRD: DeployEvent

   - Mitä kenttiä päivitetään?

3. uusi CRD: DeployEvent -operaattori-> päivitä resurssin annotaatio deploy-status(?):deploying
   - Mitä askeleita deployment:ssa on? Readiness ja Healthiness proben hyödyntäminen?
   - Miten voitaisiin määritellä sääntö, että jos esimerkiksi 2 failurea niin rollback?
     .ConfigMap? (https://shipit.dev/posts/k8s-operators-with-python-part-1.html)

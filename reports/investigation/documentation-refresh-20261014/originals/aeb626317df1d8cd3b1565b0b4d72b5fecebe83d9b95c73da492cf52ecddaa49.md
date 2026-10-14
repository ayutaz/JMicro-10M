# 教材・供給・品質・量 — 10/14

[分野一覧へ](02_material.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/06.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/06.json) ／ SHA256: `9dff7a6f1248bc950e0645478303285e9ee9ccc21ee7363aed7f495fdc142f3c` ／ 6,830 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| input.update | 320442 |
| input.reference_token_digest | "033a4b01e220afd787ad3463b8759643953c3d89574b558763bd95cdaf177e4a" |
| input.masked_token_digest | "4ee262a38c8fd9d8e385ee029fe8d2c5f4e8d2d5095363cb205bbba6e32d3338" |
| input.teachers | 30090 |
| input.teachers_by_group.web | 24523 |
| input.teachers_by_group.story | 2033 |
| input.teachers_by_group.ordinary_textbook | 3048 |
| input.teachers_by_group.conditional_outcome_body | 418 |
| input.teachers_by_group.conditional_EOS | 68 |
| input.body_bytes | 119579 |
| diagnostics.groups.web.teachers | 24523 |
| diagnostics.groups.web.teacher_fraction | 0.8149883682286474 |
| diagnostics.groups.story.teachers | 2033 |
| diagnostics.groups.story.teacher_fraction | 0.06756397474243934 |
| diagnostics.groups.ordinary_textbook.teachers | 3048 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10129611166500499 |
| diagnostics.groups.conditional_outcome_body.teachers | 418 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.013891658358258558 |
| diagnostics.groups.conditional_EOS.teachers | 68 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0022598870056497176 |
| diagnostics.groups.conditional_EOS.CE_mean | 0.040975277969504106 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.022963527590036392 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 10.161360958591104 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.0046872287057340145 |
| diagnostics.groups.independent_total.teachers | 30090 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 486 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.016151545363908275 |
| diagnostics.pairs.web__story.dot | -0.004483254626393318 |
| diagnostics.pairs.web__story.cosine | -0.06391938006729393 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.003152028191834688 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.04015366230393252 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 2.190492523368448e-06 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.00019341410464059297 |
| diagnostics.pairs.web__conditional_EOS.dot | 0.000921555794775486 |
| diagnostics.pairs.web__conditional_EOS.cosine | 0.0813897652419354 |
| diagnostics.pairs.web__independent_total.dot | 0.2427031695842743 |
| diagnostics.pairs.web__independent_total.cosine | 0.9160355806317722 |
| diagnostics.pairs.web__conditional_total.dot | 0.0009237463818863034 |
| diagnostics.pairs.web__conditional_total.cosine | 0.056866309365434756 |
| diagnostics.pairs.story__ordinary_textbook.dot | -0.00015566081856377423 |
| diagnostics.pairs.story__ordinary_textbook.cosine | -0.006873532214642334 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.00010187867155764252 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.031181373399610843 |
| diagnostics.pairs.story__conditional_EOS.dot | -4.0331065974896774e-05 |
| diagnostics.pairs.story__conditional_EOS.cosine | -0.012346773133866862 |
| diagnostics.pairs.story__independent_total.dot | 0.015655584633350372 |
| diagnostics.pairs.story__independent_total.cosine | 0.20481972220446013 |
| diagnostics.pairs.story__conditional_total.dot | 6.154761649668217e-05 |
| diagnostics.pairs.story__conditional_total.cosine | 0.013133458534549574 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | 5.2364393923198804e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | 0.014320030869106559 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | -7.107008423190564e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | -0.019440010866251425 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.028328780084848404 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.331151148248016 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | -1.870567757578101e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | -0.0035664589851731876 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 1.5226790310407523e-05 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.02886884248909173 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.0006998581811785698 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.056704792976536994 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.0005427976720966399 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7173202209654399 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.001353367930278182 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.10967999103339382 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.0005425503477454185 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.7171614669390887 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.002053226111456752 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.11598515806898015 |
| diagnostics.total_teacher_count | 30090 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/07.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/07.json) ／ SHA256: `2348090c7575df64977462dcb3a225e8778e1cd245a928cae1387c08d65e35ea` ／ 6,830 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| input.update | 320443 |
| input.reference_token_digest | "c5674bd816a81e053249e8a0c889e487ef3c6d912e4d019dd92293fdde6df3ad" |
| input.masked_token_digest | "079cfc65d26f7fd57d7f61d306ce40d164fa87eb2a4559d0ffe364e1d9e04de8" |
| input.teachers | 30157 |
| input.teachers_by_group.web | 25552 |
| input.teachers_by_group.story | 1021 |
| input.teachers_by_group.ordinary_textbook | 3048 |
| input.teachers_by_group.conditional_outcome_body | 462 |
| input.teachers_by_group.conditional_EOS | 74 |
| input.body_bytes | 119741 |
| diagnostics.groups.web.teachers | 25552 |
| diagnostics.groups.web.teacher_fraction | 0.8472991345292967 |
| diagnostics.groups.story.teachers | 1021 |
| diagnostics.groups.story.teacher_fraction | 0.03385615280034486 |
| diagnostics.groups.ordinary_textbook.teachers | 3048 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10107106144510396 |
| diagnostics.groups.conditional_outcome_body.teachers | 462 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.015319826242663395 |
| diagnostics.groups.conditional_EOS.teachers | 74 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0024538249825911064 |
| diagnostics.groups.conditional_EOS.CE_mean | 0.0030077523677735714 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.0010622183326631784 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 0.4328826791638307 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | -5.955268716206774e-05 |
| diagnostics.groups.independent_total.teachers | 30157 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 536 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.0177736512252545 |
| diagnostics.pairs.web__story.dot | -0.0014101407723501325 |
| diagnostics.pairs.web__story.cosine | -0.03262745976169559 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.0033268341794610023 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.04105231180294087 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.0006476468988694251 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.04258121947497789 |
| diagnostics.pairs.web__conditional_EOS.dot | -3.2503201509825885e-05 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.063076059640232 |
| diagnostics.pairs.web__independent_total.dot | 0.23124076426029205 |
| diagnostics.pairs.web__independent_total.cosine | 0.9275320505694067 |
| diagnostics.pairs.web__conditional_total.dot | 0.0006151437410153449 |
| diagnostics.pairs.web__conditional_total.cosine | 0.0404629140453035 |
| diagnostics.pairs.story__ordinary_textbook.dot | 3.510086389724165e-05 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.002358525784714778 |
| diagnostics.pairs.story__conditional_outcome_body.dot | -4.1405277443118393e-05 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | -0.014823538279360947 |
| diagnostics.pairs.story__conditional_EOS.dot | 1.024175276143069e-06 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.010822537298738508 |
| diagnostics.pairs.story__independent_total.dot | 0.00652099447324872 |
| diagnostics.pairs.story__independent_total.cosine | 0.14242779816439113 |
| diagnostics.pairs.story__conditional_total.dot | -4.038110637338832e-05 |
| diagnostics.pairs.story__conditional_total.cosine | -0.014463557904257853 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | 5.627875361824408e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | 0.010745492548740394 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 1.5651005014660768e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.08820286384672747 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.024687353521585464 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.28756835592553986 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 7.192975317593664e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.013740139627877221 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | -1.01833416010777e-06 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | -0.030577650014162714 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.0016449971590191126 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.1020951383516549 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.000981961959041655 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.9994258181587673 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | -1.5728115613455884e-05 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | -0.028812122270503022 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 1.0997357691167053e-07 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.0033037172251138757 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.0016292689833790064 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.10116574149015334 |
| diagnostics.total_teacher_count | 30157 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/08.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/08.json) ／ SHA256: `62e74aac215979e9e2904abc3aeaf287de3495a99f7186bf973d02f97e6a93ca` ／ 6,878 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| input.update | 320444 |
| input.reference_token_digest | "47a4b7590d8d285cb5e4aef56935829c813c3d7ff09533fdd6343dff06ad0b81" |
| input.masked_token_digest | "ff58edb0009d55ecfcdf759d22cc2c37e9b6774bbf0232932ae37234ccd40b7b" |
| input.teachers | 29216 |
| input.teachers_by_group.web | 23498 |
| input.teachers_by_group.story | 2028 |
| input.teachers_by_group.ordinary_textbook | 3049 |
| input.teachers_by_group.conditional_outcome_body | 546 |
| input.teachers_by_group.conditional_EOS | 95 |
| input.body_bytes | 113138 |
| diagnostics.groups.web.teachers | 23498 |
| diagnostics.groups.web.teacher_fraction | 0.8042853231106243 |
| diagnostics.groups.story.teachers | 2028 |
| diagnostics.groups.story.teacher_fraction | 0.06941401971522454 |
| diagnostics.groups.ordinary_textbook.teachers | 3049 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10436062431544359 |
| diagnostics.groups.conditional_outcome_body.teachers | 546 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.018688389923329683 |
| diagnostics.groups.conditional_EOS.teachers | 95 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0032516429353778753 |
| diagnostics.groups.conditional_EOS.CE_mean | 0.0015092119966682634 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.0007247618632391095 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 0.22289097469888233 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 5.674581552739255e-05 |
| diagnostics.groups.independent_total.teachers | 29216 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 641 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.021940032858707558 |
| diagnostics.pairs.web__story.dot | 0.0030991178937256336 |
| diagnostics.pairs.web__story.cosine | 0.04720396392423472 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.0022911340929567814 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.027714465468945165 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.0003147557144984603 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.02181747690506504 |
| diagnostics.pairs.web__conditional_EOS.dot | 1.3540794498112518e-05 |
| diagnostics.pairs.web__conditional_EOS.cosine | 0.03824656615154795 |
| diagnostics.pairs.web__independent_total.dot | 0.23975758254528046 |
| diagnostics.pairs.web__independent_total.cosine | 0.9159402553520355 |
| diagnostics.pairs.web__conditional_total.dot | 0.00032829653355292976 |
| diagnostics.pairs.web__conditional_total.cosine | 0.022717905405078818 |
| diagnostics.pairs.story__ordinary_textbook.dot | -0.0006334877107292414 |
| diagnostics.pairs.story__ordinary_textbook.cosine | -0.02785141536068037 |
| diagnostics.pairs.story__conditional_outcome_body.dot | -1.1939015166717581e-05 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | -0.0030078240802874313 |
| diagnostics.pairs.story__conditional_EOS.dot | 1.198014615511056e-06 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.012298821156044054 |
| diagnostics.pairs.story__independent_total.dot | 0.02052011340856552 |
| diagnostics.pairs.story__independent_total.cosine | 0.28492307170274084 |
| diagnostics.pairs.story__conditional_total.dot | -1.0740989637270104e-05 |
| diagnostics.pairs.story__conditional_total.cosine | -0.0027014650002014436 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -2.14351384784095e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.004288702145561828 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | -1.7061267953977222e-07 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | -0.0013910038617264758 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.025693027302622795 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.2833210286961502 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | -2.1605752408504486e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | -0.004315589203306963 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 1.2037105534545844e-06 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.05623594094837146 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.0011548750335350633 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.07297488051314378 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.0008734225993975997 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.9997007284185015 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 1.6294143279083073e-05 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.04195535228857084 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 1.728990127958241e-06 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.08064092928402382 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.0011711693368852139 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.07388039086297518 |
| diagnostics.total_teacher_count | 29216 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/09.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/09.json) ／ SHA256: `1f04151d86c60c51396fd759c342326e94a870d7dc109801a1e248768b54f684` ／ 6,843 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| input.update | 320445 |
| input.reference_token_digest | "ca797738dad4aee06c568011b7c4d33befd9bfad96f331135d96c8a448ec02c6" |
| input.masked_token_digest | "d5217f9dbf7d62355071ae584b678982add3fbb1a8c69869bc8790df676d642f" |
| input.teachers | 30051 |
| input.teachers_by_group.web | 25545 |
| input.teachers_by_group.story | 1013 |
| input.teachers_by_group.ordinary_textbook | 3048 |
| input.teachers_by_group.conditional_outcome_body | 374 |
| input.teachers_by_group.conditional_EOS | 71 |
| input.body_bytes | 116831 |
| diagnostics.groups.web.teachers | 25545 |
| diagnostics.groups.web.teacher_fraction | 0.8500549066586802 |
| diagnostics.groups.story.teachers | 1013 |
| diagnostics.groups.story.teacher_fraction | 0.03370936075338591 |
| diagnostics.groups.ordinary_textbook.teachers | 3048 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10142757312568633 |
| diagnostics.groups.conditional_outcome_body.teachers | 374 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.012445509300855213 |
| diagnostics.groups.conditional_EOS.teachers | 71 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0023626501613922997 |
| diagnostics.groups.conditional_EOS.CE_mean | 0.002312983937141761 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.001032829750329256 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 0.43714882855133064 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 1.7703174307825975e-05 |
| diagnostics.groups.independent_total.teachers | 30051 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 445 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.014808159462247512 |
| diagnostics.pairs.web__story.dot | -0.0015318316873162985 |
| diagnostics.pairs.web__story.cosine | -0.030709924672926832 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.003273316193372011 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.04151513024663085 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.000719976844266057 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.05028346798404056 |
| diagnostics.pairs.web__conditional_EOS.dot | -2.1442856450448744e-05 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.04266069510145806 |
| diagnostics.pairs.web__independent_total.dot | 0.2313108891248703 |
| diagnostics.pairs.web__independent_total.cosine | 0.9261976763272264 |
| diagnostics.pairs.web__conditional_total.dot | -0.0007414196734316647 |
| diagnostics.pairs.web__conditional_total.cosine | -0.05129056102075323 |
| diagnostics.pairs.story__ordinary_textbook.dot | -0.0001945208787219599 |
| diagnostics.pairs.story__ordinary_textbook.cosine | -0.011713977171661519 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 6.0957656387472525e-05 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.020214110719276708 |
| diagnostics.pairs.story__conditional_EOS.dot | 4.3258778532617725e-06 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.04086384394180568 |
| diagnostics.pairs.story__independent_total.dot | 0.008847873657941818 |
| diagnostics.pairs.story__independent_total.cosine | 0.16821557698299228 |
| diagnostics.pairs.story__conditional_total.dot | 6.528352969326079e-05 |
| diagnostics.pairs.story__conditional_total.cosine | 0.02144354816321533 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | 7.847248343750834e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | 0.016462451143111973 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 1.2896431144326925e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.077069977949594 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.02287021093070507 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.2750731483679475 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 9.136892185779288e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.018986383911724122 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 7.784123226883821e-06 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.2561613677017855 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.00029325936338864267 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.019423082848216075 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.0008734188741073012 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.9994350494721356 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 4.662125320464838e-06 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.008796072269289629 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 8.850860467646271e-06 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.288506799263965 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.00029792150598950684 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.019544959054605265 |
| diagnostics.total_teacher_count | 30051 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/10.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/10.json) ／ SHA256: `8760c6b45ed9833961b76c699e854bfff76a93804af74e4f5fbbb9482db8f884` ／ 6,844 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| input.update | 320446 |
| input.reference_token_digest | "86dd4373b924ff67c22ab788363793db17099f19882f6a934693da9bc46790dd" |
| input.masked_token_digest | "4431b596f76f0e7d99b49a1c20c6be5edeff09ef8c154daedfd201ae3e664f6c" |
| input.teachers | 30109 |
| input.teachers_by_group.web | 23505 |
| input.teachers_by_group.story | 2033 |
| input.teachers_by_group.ordinary_textbook | 4064 |
| input.teachers_by_group.conditional_outcome_body | 433 |
| input.teachers_by_group.conditional_EOS | 74 |
| input.body_bytes | 117579 |
| diagnostics.groups.web.teachers | 23505 |
| diagnostics.groups.web.teacher_fraction | 0.7806635889601116 |
| diagnostics.groups.story.teachers | 2033 |
| diagnostics.groups.story.teacher_fraction | 0.06752133913447807 |
| diagnostics.groups.ordinary_textbook.teachers | 4064 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.13497625294762364 |
| diagnostics.groups.conditional_outcome_body.teachers | 433 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.014381082068484506 |
| diagnostics.groups.conditional_EOS.teachers | 74 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.002457736889302202 |
| diagnostics.groups.conditional_EOS.CE_mean | 0.011866126410864495 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.003151253331452608 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 1.2821768453608997 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | -0.0002249676763312891 |
| diagnostics.groups.independent_total.teachers | 30109 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 507 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.01683881895778671 |
| diagnostics.pairs.web__story.dot | -0.00019967123807873577 |
| diagnostics.pairs.web__story.cosine | -0.0029035961298424203 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.005356449633836746 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.051760625363358355 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.0005102403811179101 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.024992030137700426 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.00014585682947654277 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.09565834884564503 |
| diagnostics.pairs.web__independent_total.dot | 0.22790929675102234 |
| diagnostics.pairs.web__independent_total.cosine | 0.871511400843754 |
| diagnostics.pairs.web__conditional_total.dot | -0.0006560973124578595 |
| diagnostics.pairs.web__conditional_total.cosine | -0.03199417906680319 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.001372985658235848 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.0451700235006465 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.0002984708989970386 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.04977262208810673 |
| diagnostics.pairs.story__conditional_EOS.dot | 3.311162072350271e-05 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.07393301222015833 |
| diagnostics.pairs.story__independent_total.dot | 0.021701987832784653 |
| diagnostics.pairs.story__independent_total.cosine | 0.28253511208367826 |
| diagnostics.pairs.story__conditional_total.dot | 0.00033158253063447773 |
| diagnostics.pairs.story__conditional_total.cosine | 0.055049855364918986 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.0003984364739153534 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.04415189911269543 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 3.4259166568517685e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.05083191917164513 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.04138927906751633 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.35806552476475256 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | -0.0003641772782430053 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | -0.04017715270317964 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 2.9569789603556274e-06 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.0222388430834502 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.001172938966192305 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.05143447152103525 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.00178330740891397 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.9972331870428967 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | -6.571384437847883e-05 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | -0.03858381498939125 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 1.2887377124570776e-05 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.09649492369000595 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.0011072251945734024 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.04833824058455055 |
| diagnostics.total_teacher_count | 30109 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/11.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/11.json) ／ SHA256: `6f5e12d43f4ad756c09a540b624132a8a12b0ca990979c5fdd83e7d300f7f02a` ／ 6,850 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| input.update | 320447 |
| input.reference_token_digest | "b719c1d55c79af783a628171c16a4f62eca058bc4ee1aea31aaf8fe562dba54e" |
| input.masked_token_digest | "6812b2e51cbfbf1d299ad5e011c603612bc88474bb2a3eb22a1c69630cb94dc2" |
| input.teachers | 30081 |
| input.teachers_by_group.web | 24524 |
| input.teachers_by_group.story | 2036 |
| input.teachers_by_group.ordinary_textbook | 3050 |
| input.teachers_by_group.conditional_outcome_body | 403 |
| input.teachers_by_group.conditional_EOS | 68 |
| input.body_bytes | 117804 |
| diagnostics.groups.web.teachers | 24524 |
| diagnostics.groups.web.teacher_fraction | 0.8152654499517968 |
| diagnostics.groups.story.teachers | 2036 |
| diagnostics.groups.story.teacher_fraction | 0.06768392008244407 |
| diagnostics.groups.ordinary_textbook.teachers | 3050 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.1013929058209501 |
| diagnostics.groups.conditional_outcome_body.teachers | 403 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.013397160998637013 |
| diagnostics.groups.conditional_EOS.teachers | 68 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.002260563146172002 |
| diagnostics.groups.conditional_EOS.CE_mean | 0.003239356474403073 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.0012512182584032416 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 0.553498476926881 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 2.8636886781896465e-05 |
| diagnostics.groups.independent_total.teachers | 30081 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 471 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.015657724144809017 |
| diagnostics.pairs.web__story.dot | -0.0034387612249702215 |
| diagnostics.pairs.web__story.cosine | -0.04955749933669964 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.0002283616631757468 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.0027780514758298735 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.00020419934298843145 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.01678654510835092 |
| diagnostics.pairs.web__conditional_EOS.dot | -1.4226650819182396e-05 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.023179012377876358 |
| diagnostics.pairs.web__independent_total.dot | 0.23672229051589966 |
| diagnostics.pairs.web__independent_total.cosine | 0.9090549313918388 |
| diagnostics.pairs.web__conditional_total.dot | -0.0002184259647037834 |
| diagnostics.pairs.web__conditional_total.cosine | -0.017719053374723834 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.000377615331672132 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.015930280057035444 |
| diagnostics.pairs.story__conditional_outcome_body.dot | -5.115716339787468e-05 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | -0.014583781225569891 |
| diagnostics.pairs.story__conditional_EOS.dot | -6.682716957584489e-07 |
| diagnostics.pairs.story__conditional_EOS.cosine | -0.0037757395032774316 |
| diagnostics.pairs.story__independent_total.dot | 0.01689893566071987 |
| diagnostics.pairs.story__independent_total.cosine | 0.2250437955653964 |
| diagnostics.pairs.story__conditional_total.dot | -5.182542372494936e-05 |
| diagnostics.pairs.story__conditional_total.cosine | -0.014579271318406252 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.00020447047427296638 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.04920440935479591 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 1.3907837455917615e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.06633126781620867 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.028034498915076256 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.3151448481759217 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | -0.00019056262681260705 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | -0.04525227502555758 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 7.497963451896794e-06 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.24165284595312506 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.00016345400945283473 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.012416604881040856 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.0006224435055628419 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.9988321503052353 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 8.070018338912632e-06 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.012149742993528929 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 9.0635094238678e-06 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.28825325843606636 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.00017152397776953876 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.012857644027663566 |
| diagnostics.total_teacher_count | 30081 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/12.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/12.json) ／ SHA256: `71c5a06a1ec0091c09e272c849b7a2b96902d1925a86ec089a967a9ad215cec9` ／ 6,849 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| input.update | 320448 |
| input.reference_token_digest | "89514be684433853f9230b1dc8ffed7db5cc91857b393862a0e8b6194fe64f04" |
| input.masked_token_digest | "ebc667d3a48ef9ac42787e5809ab9b80bff9b14848ebea8f1f82d68224f3794f" |
| input.teachers | 29218 |
| input.teachers_by_group.web | 24527 |
| input.teachers_by_group.story | 1018 |
| input.teachers_by_group.ordinary_textbook | 3049 |
| input.teachers_by_group.conditional_outcome_body | 530 |
| input.teachers_by_group.conditional_EOS | 94 |
| input.body_bytes | 114750 |
| diagnostics.groups.web.teachers | 24527 |
| diagnostics.groups.web.teacher_fraction | 0.83944828530358 |
| diagnostics.groups.story.teachers | 1018 |
| diagnostics.groups.story.teacher_fraction | 0.03484153603942775 |
| diagnostics.groups.ordinary_textbook.teachers | 3049 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.1043534807310562 |
| diagnostics.groups.conditional_outcome_body.teachers | 530 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.01813950304606749 |
| diagnostics.groups.conditional_EOS.teachers | 94 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0032171948798685743 |
| diagnostics.groups.conditional_EOS.CE_mean | 0.00741723488937033 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.003489892231300473 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 1.084762459724864 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | -3.597901377361268e-05 |
| diagnostics.groups.independent_total.teachers | 29218 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 624 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.02135669792593607 |
| diagnostics.pairs.web__story.dot | 0.0011851534945890307 |
| diagnostics.pairs.web__story.cosine | 0.02237685421823989 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.00597309460863471 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.06965475098733183 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.00136781414039433 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.0474044984525458 |
| diagnostics.pairs.web__conditional_EOS.dot | -8.725994121050462e-05 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.050424888088161944 |
| diagnostics.pairs.web__independent_total.dot | 0.23964598774909973 |
| diagnostics.pairs.web__independent_total.cosine | 0.9198225141427608 |
| diagnostics.pairs.web__conditional_total.dot | -0.00145507394336164 |
| diagnostics.pairs.web__conditional_total.cosine | -0.04971494092719541 |
| diagnostics.pairs.story__ordinary_textbook.dot | -0.0010022815549746156 |
| diagnostics.pairs.story__ordinary_textbook.cosine | -0.05426020684180047 |
| diagnostics.pairs.story__conditional_outcome_body.dot | -0.00046378260594792664 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | -0.07461863296934514 |
| diagnostics.pairs.story__conditional_EOS.dot | -2.904791244873195e-06 |
| diagnostics.pairs.story__conditional_EOS.cosine | -0.007792652700140421 |
| diagnostics.pairs.story__independent_total.dot | 0.011123956181108952 |
| diagnostics.pairs.story__independent_total.cosine | 0.19821362322259609 |
| diagnostics.pairs.story__conditional_total.dot | -0.0004666874301619828 |
| diagnostics.pairs.story__conditional_total.cosine | -0.07402328504726187 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | 0.00036992484820075333 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | 0.036759805853249256 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 2.5311146600870416e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.04193813177769661 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.02332967147231102 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.2567495810223178 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.0003952359256800264 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.03871912734618438 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 4.287159026716836e-05 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.21110960273150706 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.0019646300934255123 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.06425738306115832 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.003428966971114278 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.9983286962081503 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | -9.932660759659484e-06 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | -0.005416832396148325 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 5.505094304680824e-05 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.2672468419484361 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.001954697770997882 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.06302767157755247 |
| diagnostics.total_teacher_count | 29218 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/13.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/13.json) ／ SHA256: `00b9f79ec73c51673a7d644c9eac14f66f856077f07eeb337302a9da0b0ca034` ／ 6,854 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| input.update | 320449 |
| input.reference_token_digest | "bafa83fd10434309d3b4cb37b107bd91caeb82ca7c409aa55cbff0fc8d2e42d7" |
| input.masked_token_digest | "a3a8dde0b7640f4af1286fb50f11ae7c9d6e7b8debd192b574378797017a3a43" |
| input.teachers | 30121 |
| input.teachers_by_group.web | 24522 |
| input.teachers_by_group.story | 2030 |
| input.teachers_by_group.ordinary_textbook | 3047 |
| input.teachers_by_group.conditional_outcome_body | 446 |
| input.teachers_by_group.conditional_EOS | 76 |
| input.body_bytes | 119192 |
| diagnostics.groups.web.teachers | 24522 |
| diagnostics.groups.web.teacher_fraction | 0.8141163971979682 |
| diagnostics.groups.story.teachers | 2030 |
| diagnostics.groups.story.teacher_fraction | 0.06739484080873809 |
| diagnostics.groups.ordinary_textbook.teachers | 3047 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10115866007104678 |
| diagnostics.groups.conditional_outcome_body.teachers | 446 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.014806945320540487 |
| diagnostics.groups.conditional_EOS.teachers | 76 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0025231566017064506 |
| diagnostics.groups.conditional_EOS.CE_mean | 0.007637470127328446 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.0028945591766387224 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 1.1471975915728283 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | -9.636738104745746e-05 |
| diagnostics.groups.independent_total.teachers | 30121 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 522 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.01733010192224694 |
| diagnostics.pairs.web__story.dot | -0.0012944748159497976 |
| diagnostics.pairs.web__story.cosine | -0.019000834956822515 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.0017329651163890958 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.02109608195418072 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.00041527082794345915 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.019165687002728454 |
| diagnostics.pairs.web__conditional_EOS.dot | -9.941561438608915e-05 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.06919636834251024 |
| diagnostics.pairs.web__independent_total.dot | 0.24366432428359985 |
| diagnostics.pairs.web__independent_total.cosine | 0.912697892639235 |
| diagnostics.pairs.web__conditional_total.dot | 0.00031585543183609843 |
| diagnostics.pairs.web__conditional_total.cosine | 0.014491189356443999 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.0005785588873550296 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.025469264788603046 |
| diagnostics.pairs.story__conditional_outcome_body.dot | -0.0001821200712583959 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | -0.030395384547590863 |
| diagnostics.pairs.story__conditional_EOS.dot | 2.9746459404123016e-05 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.07487223916644904 |
| diagnostics.pairs.story__independent_total.dot | 0.017971940338611603 |
| diagnostics.pairs.story__independent_total.cosine | 0.24343717544399487 |
| diagnostics.pairs.story__conditional_total.dot | -0.00015237358456943184 |
| diagnostics.pairs.story__conditional_total.cosine | -0.025280299721091404 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.0003622185322456062 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.0501364291103598 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 2.6209561838186346e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.05471144622194573 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.025897612795233727 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.2909273694060457 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | -0.0003360090486239642 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | -0.046233463299165084 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 7.186687980720308e-06 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.05687589310269057 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.0017839855281636119 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.07597962792771316 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.001912806648761034 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.9978322153112547 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | -2.787931589409709e-05 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | -0.017907034598540005 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 1.556516144773923e-05 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.12245479195800293 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.0017561062704771757 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.07434972348407541 |
| diagnostics.total_teacher_count | 30121 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/14.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/14.json) ／ SHA256: `6983d474f66f51c5afc3609df4e91840d7c14dbd006ca5e2f46827cc506329f7` ／ 6,838 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| input.update | 320450 |
| input.reference_token_digest | "dc7353b5dd8461912c8cf47fdb2ce71ab7e356514d08b7158ceab7299ebfffd3" |
| input.masked_token_digest | "211f09467752625c85171233ee53695c8649abd4ba2d692b222fc25036b8ef0e" |
| input.teachers | 30093 |
| input.teachers_by_group.web | 25543 |
| input.teachers_by_group.story | 1015 |
| input.teachers_by_group.ordinary_textbook | 3048 |
| input.teachers_by_group.conditional_outcome_body | 418 |
| input.teachers_by_group.conditional_EOS | 69 |
| input.body_bytes | 117837 |
| diagnostics.groups.web.teachers | 25543 |
| diagnostics.groups.web.teacher_fraction | 0.8488020469876716 |
| diagnostics.groups.story.teachers | 1015 |
| diagnostics.groups.story.teacher_fraction | 0.03372877413351942 |
| diagnostics.groups.ordinary_textbook.teachers | 3048 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10128601335858838 |
| diagnostics.groups.conditional_outcome_body.teachers | 418 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.013890273485528196 |
| diagnostics.groups.conditional_EOS.teachers | 69 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0022928920346924533 |
| diagnostics.groups.conditional_EOS.CE_mean | 0.0012576523088458655 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.0005826930282637477 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 0.2541301637614632 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 1.816019539546687e-05 |
| diagnostics.groups.independent_total.teachers | 30093 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 487 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.01618316552022065 |
| diagnostics.pairs.web__story.dot | -0.0014554883819073439 |
| diagnostics.pairs.web__story.cosine | -0.027316840752629714 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.0029381641652435064 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.03458891492961373 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.0003228105488233268 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.027808379895887612 |
| diagnostics.pairs.web__conditional_EOS.dot | 1.0758497410279233e-05 |
| diagnostics.pairs.web__conditional_EOS.cosine | 0.03494443922157837 |
| diagnostics.pairs.web__independent_total.dot | 0.2751196622848511 |
| diagnostics.pairs.web__independent_total.cosine | 0.9396723503463709 |
| diagnostics.pairs.web__conditional_total.dot | 0.00033356909989379346 |
| diagnostics.pairs.web__conditional_total.cosine | 0.028671240004169 |
| diagnostics.pairs.story__ordinary_textbook.dot | -0.00013191657490096986 |
| diagnostics.pairs.story__ordinary_textbook.cosine | -0.00813672073498461 |
| diagnostics.pairs.story__conditional_outcome_body.dot | -6.186468090163544e-05 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | -0.02792286227675548 |
| diagnostics.pairs.story__conditional_EOS.dot | -1.4185047803039197e-05 |
| diagnostics.pairs.story__conditional_EOS.cosine | -0.24140509408106353 |
| diagnostics.pairs.story__independent_total.dot | 0.008509565144777298 |
| diagnostics.pairs.story__independent_total.cosine | 0.15228296549617035 |
| diagnostics.pairs.story__conditional_total.dot | -7.604974234709516e-05 |
| diagnostics.pairs.story__conditional_total.cosine | -0.03424897323172725 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -6.808618491049856e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.01927592702319726 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 7.783268301864155e-06 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.08308388151763013 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.022723669186234474 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.2550712859487544 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | -6.030290751368739e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | -0.017034415149414093 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 9.077506319954409e-07 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.07090688782958858 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.0006772541673853993 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.05562907973620415 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.00048360705841332674 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.9996516748903077 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 5.5762666306691244e-06 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.01726999539043901 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 1.2472818298192578e-06 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.0972118405137069 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.0006828304030932486 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.055962324153993576 |
| diagnostics.total_teacher_count | 30093 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/15.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/completed_masked_mixed/15.json) ／ SHA256: `6aaaf6f09284f6ef76078619922141e34830731589d0505917108ba9982d1083` ／ 6,864 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| input.update | 320451 |
| input.reference_token_digest | "8df15572536212e7143ef5ed7c26a0c70244e20de9546a3d0f74ffd26ec573a3" |
| input.masked_token_digest | "83950ca52e867264576e3f491e376baaa850aab75a4159dd6871d0da3a643770" |
| input.teachers | 30027 |
| input.teachers_by_group.web | 23501 |
| input.teachers_by_group.story | 2029 |
| input.teachers_by_group.ordinary_textbook | 4067 |
| input.teachers_by_group.conditional_outcome_body | 366 |
| input.teachers_by_group.conditional_EOS | 64 |
| input.body_bytes | 119949 |
| diagnostics.groups.web.teachers | 23501 |
| diagnostics.groups.web.teacher_fraction | 0.7826622706231059 |
| diagnostics.groups.story.teachers | 2029 |
| diagnostics.groups.story.teacher_fraction | 0.06757251806707297 |
| diagnostics.groups.ordinary_textbook.teachers | 4067 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.13544476637692743 |
| diagnostics.groups.conditional_outcome_body.teachers | 366 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.012189029873114198 |
| diagnostics.groups.conditional_EOS.teachers | 64 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.002131415059779532 |
| diagnostics.groups.conditional_EOS.CE_mean | 0.0038632212672382593 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.0013883095234632492 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 0.6513557822036091 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 2.229713754786644e-05 |
| diagnostics.groups.independent_total.teachers | 30027 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 430 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.01432044493289373 |
| diagnostics.pairs.web__story.dot | -0.00016437997692264616 |
| diagnostics.pairs.web__story.cosine | -0.002476746532643522 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.005555581301450729 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.056700159205966986 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.0005676033324562013 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.03758578933807359 |
| diagnostics.pairs.web__conditional_EOS.dot | -8.826764315017499e-06 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.012925058666328459 |
| diagnostics.pairs.web__independent_total.dot | 0.23566466569900513 |
| diagnostics.pairs.web__independent_total.cosine | 0.8891368835119157 |
| diagnostics.pairs.web__conditional_total.dot | -0.0005764300585724413 |
| diagnostics.pairs.web__conditional_total.cosine | -0.03807748704495544 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.001287729013711214 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.04791563686638346 |
| diagnostics.pairs.story__conditional_outcome_body.dot | -0.0002476345980539918 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | -0.05978442514778002 |
| diagnostics.pairs.story__conditional_EOS.dot | -5.489682735060342e-07 |
| diagnostics.pairs.story__conditional_EOS.cosine | -0.0029307330901104105 |
| diagnostics.pairs.story__independent_total.dot | 0.019079413264989853 |
| diagnostics.pairs.story__independent_total.cosine | 0.26244432348881847 |
| diagnostics.pairs.story__conditional_total.dot | -0.0002481835545040667 |
| diagnostics.pairs.story__conditional_total.cosine | -0.059771295811154285 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | 1.2114771379856393e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | 0.001981135052768793 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 1.2592752682394348e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.04553777567732233 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.03543802350759506 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.3301899045732279 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 2.4707525881240144e-05 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.004030612551566749 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 1.3359373269850039e-06 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.031344489358424085 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.00014103669673204422 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.00852609959249121 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.0009438268607482314 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.9989829545699582 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 6.473444045695942e-06 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.008653781490716123 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 3.2633408864057856e-06 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.07638014281315746 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.00014751017442904413 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.008895762626999005 |
| diagnostics.total_teacher_count | 30027 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/00.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/00.json) ／ SHA256: `49800132a1ee881c46300b135209797908a96400cc6b1632bfb5c29e4ae1a0cf` ／ 6,777 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320436 |
| input.reference_token_digest | "b9b1d603d51ffd5d7512a1c9b9e0035c4a23663a54ed005893aa7dcf5d4b794d" |
| input.masked_token_digest | "f362acbb1a424905aede35ea1171194c0d68fd76160e713e0a22a24bfce886aa" |
| input.teachers | 29225 |
| input.teachers_by_group.web | 23506 |
| input.teachers_by_group.story | 2033 |
| input.teachers_by_group.ordinary_textbook | 3053 |
| input.teachers_by_group.conditional_outcome_body | 542 |
| input.teachers_by_group.conditional_EOS | 91 |
| input.body_bytes | 118116 |
| diagnostics.groups.web.teachers | 23506 |
| diagnostics.groups.web.teacher_fraction | 0.8043113772455089 |
| diagnostics.groups.story.teachers | 2033 |
| diagnostics.groups.story.teacher_fraction | 0.06956372968349016 |
| diagnostics.groups.ordinary_textbook.teachers | 3053 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10446535500427716 |
| diagnostics.groups.conditional_outcome_body.teachers | 542 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.018545765611633874 |
| diagnostics.groups.conditional_EOS.teachers | 91 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0031137724550898203 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.517586341271033 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.23137080669403076 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 74.30562445750603 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.12540854513645172 |
| diagnostics.groups.independent_total.teachers | 29225 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 633 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.021659538066723695 |
| diagnostics.pairs.web__story.dot | 0.000834605481941253 |
| diagnostics.pairs.web__story.cosine | 0.008312560492455618 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.005057543516159058 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.04902846200693609 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.002451125532388687 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.020559268445516716 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.006536472123116255 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.05929891960722183 |
| diagnostics.pairs.web__independent_total.dot | 0.22389936447143555 |
| diagnostics.pairs.web__independent_total.cosine | 0.6786874281028104 |
| diagnostics.pairs.web__conditional_total.dot | -0.008987597189843655 |
| diagnostics.pairs.web__conditional_total.cosine | -0.05426338835477458 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.0060118124820292 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.1317479248348338 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.008434919640421867 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.15993841446599594 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.006774250417947769 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.13892946364388625 |
| diagnostics.pairs.story__independent_total.dot | 0.06646807491779327 |
| diagnostics.pairs.story__independent_total.cosine | 0.4554699831335286 |
| diagnostics.pairs.story__conditional_total.dot | 0.015209170058369637 |
| diagnostics.pairs.story__conditional_total.cosine | 0.20758622544641903 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.0019662026315927505 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.036287343223346896 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.004020533990114927 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.08025496149374452 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.0599965825676918 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.4001549713780497 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.0020543313585221767 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.027290943365151095 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0023539019748568535 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.040654629019470985 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.06899876147508621 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.39817729925251066 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.0649777352809906 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.746871949109868 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.06013358756899834 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.3753302453083449 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.055886346846818924 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6947819787582632 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.12913234531879425 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.5364032876495262 |
| diagnostics.total_teacher_count | 29225 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/01.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/01.json) ／ SHA256: `2f9e2a40f182b57786a263742f1881856f1cdd16763a2b23f2cb8cfa5cbc40be` ／ 6,759 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320437 |
| input.reference_token_digest | "d7731dcb8612237b8b4f0b03130d392765afc7b425384d3be2c73392a7a5df80" |
| input.masked_token_digest | "b58cea2c97d4ad2881e9e0dfb53bdafaf0bae990ea0e6b6a68d8a80489f82e99" |
| input.teachers | 30097 |
| input.teachers_by_group.web | 23500 |
| input.teachers_by_group.story | 2034 |
| input.teachers_by_group.ordinary_textbook | 4065 |
| input.teachers_by_group.conditional_outcome_body | 425 |
| input.teachers_by_group.conditional_EOS | 73 |
| input.body_bytes | 117984 |
| diagnostics.groups.web.teachers | 23500 |
| diagnostics.groups.web.teacher_fraction | 0.7808087184769246 |
| diagnostics.groups.story.teachers | 2034 |
| diagnostics.groups.story.teacher_fraction | 0.06758148652689637 |
| diagnostics.groups.ordinary_textbook.teachers | 4065 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.13506329534505102 |
| diagnostics.groups.conditional_outcome_body.teachers | 425 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.014121008738412466 |
| diagnostics.groups.conditional_EOS.teachers | 73 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.002425490912715553 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.640154276808647 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.18222147226333618 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 75.12766644807711 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.08955774456262589 |
| diagnostics.groups.independent_total.teachers | 30097 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 498 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.01654649965112802 |
| diagnostics.pairs.web__story.dot | -0.005779978819191456 |
| diagnostics.pairs.web__story.cosine | -0.057676272419585985 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.011873912066221237 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.08770029030379599 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.003336596302688122 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.032793683287083805 |
| diagnostics.pairs.web__conditional_EOS.dot | 0.0009407441830262542 |
| diagnostics.pairs.web__conditional_EOS.cosine | 0.010722597461640029 |
| diagnostics.pairs.web__independent_total.dot | 0.24218277633190155 |
| diagnostics.pairs.web__independent_total.cosine | 0.7073269651347744 |
| diagnostics.pairs.web__conditional_total.dot | 0.004277340602129698 |
| diagnostics.pairs.web__conditional_total.cosine | 0.03128613114067264 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.007642236538231373 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.13056974809224195 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.007555011194199324 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.17176574910969952 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.002668216824531555 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.07035006485519994 |
| diagnostics.pairs.story__independent_total.dot | 0.0554049089550972 |
| diagnostics.pairs.story__independent_total.cosine | 0.37431750156772664 |
| diagnostics.pairs.story__conditional_total.dot | 0.010223228484392166 |
| diagnostics.pairs.story__conditional_total.cosine | 0.17297406766523896 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | 0.00011321564670652151 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | 0.0019052156866014808 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.007086878642439842 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.1383039637472629 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.10580174624919891 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.5290795207771221 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.0072000958025455475 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.09017112144384197 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.001384807052090764 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.03596236473891607 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.0570337250828743 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.37952397039579594 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.046041131019592285 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7672811232994771 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.04529030621051788 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.3495060324492748 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.034589480608701706 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6684893506575788 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.10232402384281158 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.5067299452251773 |
| diagnostics.total_teacher_count | 30097 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/02.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/02.json) ／ SHA256: `2b25399429d52ef9344977ed679af2046edb20258de04ef2859b64df57e57bdf` ／ 6,764 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320438 |
| input.reference_token_digest | "f8a566084ad12a42e71d046e79d3f521ea01fa00cba155679b01f44bcaadf202" |
| input.masked_token_digest | "1f67f76fdca2a6108287ea0b246d7ceae7f00f8c89429d3f09b0783d3037da61" |
| input.teachers | 30137 |
| input.teachers_by_group.web | 25547 |
| input.teachers_by_group.story | 1015 |
| input.teachers_by_group.ordinary_textbook | 3059 |
| input.teachers_by_group.conditional_outcome_body | 446 |
| input.teachers_by_group.conditional_EOS | 70 |
| input.body_bytes | 117500 |
| diagnostics.groups.web.teachers | 25547 |
| diagnostics.groups.web.teacher_fraction | 0.8476955237747619 |
| diagnostics.groups.story.teachers | 1015 |
| diagnostics.groups.story.teacher_fraction | 0.033679530145668116 |
| diagnostics.groups.ordinary_textbook.teachers | 3059 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10150313568039288 |
| diagnostics.groups.conditional_outcome_body.teachers | 446 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.014799084182234462 |
| diagnostics.groups.conditional_EOS.teachers | 70 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0023227262169426286 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.6539722987583705 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.17421793937683105 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 75.00580055713654 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.0767434760928154 |
| diagnostics.groups.independent_total.teachers | 30137 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 516 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.017121810399177092 |
| diagnostics.pairs.web__story.dot | 0.00028432035469450057 |
| diagnostics.pairs.web__story.cosine | 0.0045075339532691374 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.0014045985881239176 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.01441100294439333 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.009252024814486504 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.09200355941836309 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.002655928023159504 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.031337759608002655 |
| diagnostics.pairs.web__independent_total.dot | 0.24210751056671143 |
| diagnostics.pairs.web__independent_total.cosine | 0.7992796449622521 |
| diagnostics.pairs.web__conditional_total.dot | 0.006596095860004425 |
| diagnostics.pairs.web__conditional_total.cosine | 0.049894930810335206 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.0020307968370616436 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.0781718710946356 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.003911459818482399 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.1459314065425974 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.0018624772783368826 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.08244886246182995 |
| diagnostics.pairs.story__independent_total.dot | 0.02489929273724556 |
| diagnostics.pairs.story__independent_total.cosine | 0.30840368697241693 |
| diagnostics.pairs.story__conditional_total.dot | 0.005773937329649925 |
| diagnostics.pairs.story__conditional_total.cosine | 0.16386400656416208 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.0029477467760443687 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.07117229974801681 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | -0.00019273796351626515 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | -0.005521688008749713 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.037636056542396545 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.3016807113641621 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | -0.0031404849141836166 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | -0.057679188173042455 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0003830109490081668 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.010635101739931154 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.05332585424184799 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.41429254957311623 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.04311502352356911 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.767497425837358 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.029754286631941795 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.2742853701886682 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.03073490411043167 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6491782330407168 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.08308014273643494 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.49098495275886633 |
| diagnostics.total_teacher_count | 30137 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/03.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/03.json) ／ SHA256: `1270628274c59348bc087db632521ca539403494caf5f0230dd5db8000c67ee1` ／ 6,774 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320439 |
| input.reference_token_digest | "17d84034595dfaac471c85d5cd4138ffd0fe8c50005c43797dd4f31f070a429d" |
| input.masked_token_digest | "d48890c930086379b555cdadc474ab265078eb1f4158cf51a4e4947129bf1892" |
| input.teachers | 30095 |
| input.teachers_by_group.web | 24524 |
| input.teachers_by_group.story | 2035 |
| input.teachers_by_group.ordinary_textbook | 3052 |
| input.teachers_by_group.conditional_outcome_body | 417 |
| input.teachers_by_group.conditional_EOS | 67 |
| input.body_bytes | 118762 |
| diagnostics.groups.web.teachers | 24524 |
| diagnostics.groups.web.teacher_fraction | 0.814886193719887 |
| diagnostics.groups.story.teachers | 2035 |
| diagnostics.groups.story.teacher_fraction | 0.06761920584814753 |
| diagnostics.groups.ordinary_textbook.teachers | 3052 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10141219471673035 |
| diagnostics.groups.conditional_outcome_body.teachers | 417 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.013856122279448413 |
| diagnostics.groups.conditional_EOS.teachers | 67 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0022262834357866753 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.58607983945021 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.1675192266702652 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 75.24613621853182 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.07022371888160706 |
| diagnostics.groups.independent_total.teachers | 30095 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 484 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.016082405715235087 |
| diagnostics.pairs.web__story.dot | -0.0027562016621232033 |
| diagnostics.pairs.web__story.cosine | -0.02967683252660161 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.004587160423398018 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.043746651117120894 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.002976037096232176 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.033335870778611866 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.004457442089915276 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.05631708841807662 |
| diagnostics.pairs.web__independent_total.dot | 0.22357556223869324 |
| diagnostics.pairs.web__independent_total.cosine | 0.7302368505891771 |
| diagnostics.pairs.web__conditional_total.dot | -0.0014814042951911688 |
| diagnostics.pairs.web__conditional_total.cosine | -0.012253806567185813 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.010774068534374237 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.24697266261288175 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.006460023112595081 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.17393053387399163 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.0028660602401942015 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.08703783026568325 |
| diagnostics.pairs.story__independent_total.dot | 0.055980075150728226 |
| diagnostics.pairs.story__independent_total.cosine | 0.43948208799774363 |
| diagnostics.pairs.story__conditional_total.dot | 0.009326082654297352 |
| diagnostics.pairs.story__conditional_total.cosine | 0.1854235820726605 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.0009411581559106708 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.02244391879064481 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.002162726130336523 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.05817261820902216 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.06583720445632935 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.457797501907291 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.0012215673923492432 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.021511835012428388 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0008527878671884537 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.026942054431027207 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.045044563710689545 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.36788916091126667 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.03655468672513962 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7560938003858072 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.029487859457731247 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.2716432107651548 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.02891547605395317 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6745963210658741 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.07453242689371109 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.44951462121743857 |
| diagnostics.total_teacher_count | 30095 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/04.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/04.json) ／ SHA256: `814afb331676e7ec9d022bb38863624a39e2ae6ca8b3df8b464aacb7793a22d8` ／ 6,782 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320440 |
| input.reference_token_digest | "9b2b600c87688c475b60424cd434c54a12a86eee79e2f8a6f6bd3dc0dbfe26de" |
| input.masked_token_digest | "3501daf8f94a3baa8264e1db2ef603425d60a5ec76ecb3174aacff34ae24f654" |
| input.teachers | 29248 |
| input.teachers_by_group.web | 24525 |
| input.teachers_by_group.story | 1019 |
| input.teachers_by_group.ordinary_textbook | 3048 |
| input.teachers_by_group.conditional_outcome_body | 566 |
| input.teachers_by_group.conditional_EOS | 90 |
| input.body_bytes | 118580 |
| diagnostics.groups.web.teachers | 24525 |
| diagnostics.groups.web.teacher_fraction | 0.8385188730853391 |
| diagnostics.groups.story.teachers | 1019 |
| diagnostics.groups.story.teacher_fraction | 0.034839989059080964 |
| diagnostics.groups.ordinary_textbook.teachers | 3048 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10421225382932166 |
| diagnostics.groups.conditional_outcome_body.teachers | 566 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.01935175054704595 |
| diagnostics.groups.conditional_EOS.teachers | 90 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0030771334792122538 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.486758253309461 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.2300972193479538 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 74.77648301654392 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.11136291921138763 |
| diagnostics.groups.independent_total.teachers | 29248 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 656 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.022428884026258207 |
| diagnostics.pairs.web__story.dot | 0.005721575580537319 |
| diagnostics.pairs.web__story.cosine | 0.09516270101132931 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.010436017997562885 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.09119318096737133 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.007626958191394806 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.060922965915567125 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.0058925156481564045 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.05187038219643453 |
| diagnostics.pairs.web__independent_total.dot | 0.2616319954395294 |
| diagnostics.pairs.web__independent_total.cosine | 0.7513410487982831 |
| diagnostics.pairs.web__conditional_total.dot | 0.0017344431253150105 |
| diagnostics.pairs.web__conditional_total.cosine | 0.010037327891095864 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.004426885396242142 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.15682552150659176 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.00706909503787756 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.22892036349874967 |
| diagnostics.pairs.story__conditional_EOS.dot | 2.170301740989089e-05 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.0007745149160868743 |
| diagnostics.pairs.story__independent_total.dot | 0.032070424407720566 |
| diagnostics.pairs.story__independent_total.cosine | 0.37337216407066454 |
| diagnostics.pairs.story__conditional_total.dot | 0.007090798579156399 |
| diagnostics.pairs.story__conditional_total.cosine | 0.16635816817225468 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.0037667788565158844 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.06408658972374183 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.005694261752068996 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.10676366913065037 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.07051806151866913 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.43133431271878264 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.001927482197061181 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.023758324523912445 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0026295091956853867 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.04506744280482385 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.07785540074110031 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.43531588555184053 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.06692802160978317 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7541114856654272 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.05539980158209801 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.34136032330004923 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.055574238300323486 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6900652065329946 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.1332552134990692 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.5397944030940642 |
| diagnostics.total_teacher_count | 29248 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/05.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/05.json) ／ SHA256: `71c0dd23076a3c14e00dc88026ed523ea78062c188bf4007af548003c42bb7dd` ／ 6,752 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320441 |
| input.reference_token_digest | "0e0178dddbd265701e06f3596ec11ac9cf36c1be6be6ccb27daf99831a51fd9e" |
| input.masked_token_digest | "cc38225d5b359de1e397b13d2edc4325a004ad6f293c28a57bf49629323dcc6a" |
| input.teachers | 30146 |
| input.teachers_by_group.web | 23510 |
| input.teachers_by_group.story | 2033 |
| input.teachers_by_group.ordinary_textbook | 4066 |
| input.teachers_by_group.conditional_outcome_body | 466 |
| input.teachers_by_group.conditional_EOS | 71 |
| input.body_bytes | 117947 |
| diagnostics.groups.web.teachers | 23510 |
| diagnostics.groups.web.teacher_fraction | 0.779871293040536 |
| diagnostics.groups.story.teachers | 2033 |
| diagnostics.groups.story.teacher_fraction | 0.0674384661314934 |
| diagnostics.groups.ordinary_textbook.teachers | 4066 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.1348769322629868 |
| diagnostics.groups.conditional_outcome_body.teachers | 466 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.015458103894380681 |
| diagnostics.groups.conditional_EOS.teachers | 71 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.002355204670603065 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.805553597463688 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.17526252567768097 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 74.41498731097705 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.07573592662811279 |
| diagnostics.groups.independent_total.teachers | 30146 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 537 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.017813308564983747 |
| diagnostics.pairs.web__story.dot | 0.0033777616918087006 |
| diagnostics.pairs.web__story.cosine | 0.034069911346409125 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.010077259503304958 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.07554789877993674 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.006050728727132082 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.065907511791269 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.0025665410794317722 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.03220183034486098 |
| diagnostics.pairs.web__independent_total.dot | 0.22375471889972687 |
| diagnostics.pairs.web__independent_total.cosine | 0.6825342893830751 |
| diagnostics.pairs.web__conditional_total.dot | 0.0034841878805309534 |
| diagnostics.pairs.web__conditional_total.cosine | 0.0285116722837687 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.014631510712206364 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.22880646371507782 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.010207083076238632 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.2319145818818973 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.0034175878390669823 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.08944400429923184 |
| diagnostics.pairs.story__independent_total.dot | 0.07916541397571564 |
| diagnostics.pairs.story__independent_total.cosine | 0.503717412375686 |
| diagnostics.pairs.story__conditional_total.dot | 0.013624669052660465 |
| diagnostics.pairs.story__conditional_total.cosine | 0.23256602565158302 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | 0.000938085257075727 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | 0.015841878729188828 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.007420339621603489 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.1443421803218673 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.11907894909381866 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.5631504107323162 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.00835842452943325 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.10604316255026032 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.00036893735523335636 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.010427240659207257 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.05832581967115402 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.40077213186661964 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.04112463817000389 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7580670857079916 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.03935864940285683 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.3115171746902182 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.031085889786481857 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6600456353548945 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.09768445789813995 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.5042617878001363 |
| diagnostics.total_teacher_count | 30146 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/06.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/06.json) ／ SHA256: `bca5977fcf46016984f0383f9dbb8516063dccefcb89713aa5b79d1e0e0c662d` ／ 6,772 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320442 |
| input.reference_token_digest | "033a4b01e220afd787ad3463b8759643953c3d89574b558763bd95cdaf177e4a" |
| input.masked_token_digest | "4ee262a38c8fd9d8e385ee029fe8d2c5f4e8d2d5095363cb205bbba6e32d3338" |
| input.teachers | 30090 |
| input.teachers_by_group.web | 24523 |
| input.teachers_by_group.story | 2033 |
| input.teachers_by_group.ordinary_textbook | 3048 |
| input.teachers_by_group.conditional_outcome_body | 418 |
| input.teachers_by_group.conditional_EOS | 68 |
| input.body_bytes | 119579 |
| diagnostics.groups.web.teachers | 24523 |
| diagnostics.groups.web.teacher_fraction | 0.8149883682286474 |
| diagnostics.groups.story.teachers | 2033 |
| diagnostics.groups.story.teacher_fraction | 0.06756397474243934 |
| diagnostics.groups.ordinary_textbook.teachers | 3048 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10129611166500499 |
| diagnostics.groups.conditional_outcome_body.teachers | 418 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.013891658358258558 |
| diagnostics.groups.conditional_EOS.teachers | 68 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0022598870056497176 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.541177188648897 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.1697768121957779 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 75.12623939663172 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.08635568618774414 |
| diagnostics.groups.independent_total.teachers | 30090 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 486 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.016151545363908275 |
| diagnostics.pairs.web__story.dot | -0.00865869503468275 |
| diagnostics.pairs.web__story.cosine | -0.0838408069809434 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.007623441983014345 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.07563272209512475 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.0028435522690415382 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.03220633014450081 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.0008511908235959709 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.010533528213459657 |
| diagnostics.pairs.web__independent_total.dot | 0.22180435061454773 |
| diagnostics.pairs.web__independent_total.cosine | 0.7140195277726265 |
| diagnostics.pairs.web__conditional_total.dot | -0.0036947433836758137 |
| diagnostics.pairs.web__conditional_total.cosine | -0.030320739609507565 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.008432718925178051 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.18351799925202925 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.00972341001033783 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.24157446724621778 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.0032515604980289936 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.08826553427330565 |
| diagnostics.pairs.story__independent_total.dot | 0.05982905626296997 |
| diagnostics.pairs.story__independent_total.cosine | 0.42247850916033364 |
| diagnostics.pairs.story__conditional_total.dot | 0.012974970042705536 |
| diagnostics.pairs.story__conditional_total.cosine | 0.23356851966997552 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.00010259145346935838 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.0026115554221158264 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.004408418200910091 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.12261334765958505 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.06520716845989227 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.4717842348703266 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.0043058255687355995 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.07941819237962437 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.00115518260281533 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.036679802667959935 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.042346060276031494 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.349769946979956 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.03556564450263977 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7488859170073179 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.03678421303629875 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.3319692281044654 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.029979348182678223 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6897219641038642 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.07913026958703995 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.4735737476209136 |
| diagnostics.total_teacher_count | 30090 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/07.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/07.json) ／ SHA256: `15b047472bfb4b97171f7ec177cabb30a498e763c09fb4812d36516b9baf6ea0` ／ 6,761 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320443 |
| input.reference_token_digest | "c5674bd816a81e053249e8a0c889e487ef3c6d912e4d019dd92293fdde6df3ad" |
| input.masked_token_digest | "079cfc65d26f7fd57d7f61d306ce40d164fa87eb2a4559d0ffe364e1d9e04de8" |
| input.teachers | 30157 |
| input.teachers_by_group.web | 25552 |
| input.teachers_by_group.story | 1021 |
| input.teachers_by_group.ordinary_textbook | 3048 |
| input.teachers_by_group.conditional_outcome_body | 462 |
| input.teachers_by_group.conditional_EOS | 74 |
| input.body_bytes | 119741 |
| diagnostics.groups.web.teachers | 25552 |
| diagnostics.groups.web.teacher_fraction | 0.8472991345292967 |
| diagnostics.groups.story.teachers | 1021 |
| diagnostics.groups.story.teacher_fraction | 0.03385615280034486 |
| diagnostics.groups.ordinary_textbook.teachers | 3048 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10107106144510396 |
| diagnostics.groups.conditional_outcome_body.teachers | 462 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.015319826242663395 |
| diagnostics.groups.conditional_EOS.teachers | 74 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0024538249825911064 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.760758477288324 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.1823020875453949 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 74.29302775819559 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.09076861292123795 |
| diagnostics.groups.independent_total.teachers | 30157 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 536 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.0177736512252545 |
| diagnostics.pairs.web__story.dot | 0.002169279847294092 |
| diagnostics.pairs.web__story.cosine | 0.04193389116849411 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.0005567844491451979 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.005191230906527986 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.003861608449369669 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.042834009511647494 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.0023809275589883327 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.028386539362985335 |
| diagnostics.pairs.web__independent_total.dot | 0.21587201952934265 |
| diagnostics.pairs.web__independent_total.cosine | 0.7537236594685438 |
| diagnostics.pairs.web__conditional_total.dot | 0.0014806808903813362 |
| diagnostics.pairs.web__conditional_total.cosine | 0.011907220936003255 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.0038406476378440857 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.14652828785642655 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.003756679128855467 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.1705133268031313 |
| diagnostics.pairs.story__conditional_EOS.dot | -0.0007817130535840988 |
| diagnostics.pairs.story__conditional_EOS.cosine | -0.03813707643645029 |
| diagnostics.pairs.story__independent_total.dot | 0.021627437323331833 |
| diagnostics.pairs.story__independent_total.cosine | 0.3089972314867921 |
| diagnostics.pairs.story__conditional_total.dot | 0.002974966075271368 |
| diagnostics.pairs.story__conditional_total.cosine | 0.0978959459648309 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | 0.0024994947016239166 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | 0.05471924573166102 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.0043930537067353725 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.10337135065809144 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.06563631445169449 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.4523008123135513 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.006892548408359289 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.10939467408481657 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0007102759554982185 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.019883737494921214 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.04921847581863403 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.4035046676738618 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.03910529986023903 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7383957601880828 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.03517385572195053 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.3099461085176248 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.033944327384233475 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6889164936851508 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.08439233899116516 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.5015934866146061 |
| diagnostics.total_teacher_count | 30157 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/08.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/08.json) ／ SHA256: `1ba2ceb23c101708967db387c568eb5df35e029883b1a66ef44a20d7ae30c6da` ／ 6,769 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320444 |
| input.reference_token_digest | "47a4b7590d8d285cb5e4aef56935829c813c3d7ff09533fdd6343dff06ad0b81" |
| input.masked_token_digest | "ff58edb0009d55ecfcdf759d22cc2c37e9b6774bbf0232932ae37234ccd40b7b" |
| input.teachers | 29216 |
| input.teachers_by_group.web | 23498 |
| input.teachers_by_group.story | 2028 |
| input.teachers_by_group.ordinary_textbook | 3049 |
| input.teachers_by_group.conditional_outcome_body | 546 |
| input.teachers_by_group.conditional_EOS | 95 |
| input.body_bytes | 113138 |
| diagnostics.groups.web.teachers | 23498 |
| diagnostics.groups.web.teacher_fraction | 0.8042853231106243 |
| diagnostics.groups.story.teachers | 2028 |
| diagnostics.groups.story.teacher_fraction | 0.06941401971522454 |
| diagnostics.groups.ordinary_textbook.teachers | 3049 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10436062431544359 |
| diagnostics.groups.conditional_outcome_body.teachers | 546 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.018688389923329683 |
| diagnostics.groups.conditional_EOS.teachers | 95 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0032516429353778753 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.6555726703844575 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.2396923303604126 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 73.71422235589279 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.14242440462112427 |
| diagnostics.groups.independent_total.teachers | 29216 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 641 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.021940032858707558 |
| diagnostics.pairs.web__story.dot | 0.006310240365564823 |
| diagnostics.pairs.web__story.cosine | 0.05507149541105619 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.0017488631419837475 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.015904526772978968 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.001195704797282815 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.010252513078144846 |
| diagnostics.pairs.web__conditional_EOS.dot | 0.0020378543995320797 |
| diagnostics.pairs.web__conditional_EOS.cosine | 0.018097417462795633 |
| diagnostics.pairs.web__independent_total.dot | 0.2296142280101776 |
| diagnostics.pairs.web__independent_total.cosine | 0.6746750325731459 |
| diagnostics.pairs.web__conditional_total.dot | 0.0008421488455496728 |
| diagnostics.pairs.web__conditional_total.cosine | 0.00512324726671137 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.004008156247437 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.07020940902739269 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.014344754628837109 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.23691101417218116 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.008066413924098015 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.13797796353305058 |
| diagnostics.pairs.story__independent_total.dot | 0.092214435338974 |
| diagnostics.pairs.story__independent_total.cosine | 0.521891833291293 |
| diagnostics.pairs.story__conditional_total.dot | 0.02241116762161255 |
| diagnostics.pairs.story__conditional_total.cosine | 0.26260725688817 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.0071353428065776825 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.12279788896100012 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.005518794991075993 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.09836881459967622 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.0589274987578392 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.3475230129038177 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | -0.0016165482811629772 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | -0.01973853200326014 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0016736851539462805 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.02812732130654597 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.06930817663669586 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.3853820248412364 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.06330231577157974 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.728764507990701 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.07474599778652191 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.43045922799964437 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.0591261051595211 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.704991699940639 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.14405417442321777 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.5683069103937022 |
| diagnostics.total_teacher_count | 29216 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/09.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/09.json) ／ SHA256: `480cc428fafff0a6fc96ef509d0c71da375e9a2bcc127592ddde0f8db320266c` ／ 6,739 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320445 |
| input.reference_token_digest | "ca797738dad4aee06c568011b7c4d33befd9bfad96f331135d96c8a448ec02c6" |
| input.masked_token_digest | "d5217f9dbf7d62355071ae584b678982add3fbb1a8c69869bc8790df676d642f" |
| input.teachers | 30051 |
| input.teachers_by_group.web | 25545 |
| input.teachers_by_group.story | 1013 |
| input.teachers_by_group.ordinary_textbook | 3048 |
| input.teachers_by_group.conditional_outcome_body | 374 |
| input.teachers_by_group.conditional_EOS | 71 |
| input.body_bytes | 116831 |
| diagnostics.groups.web.teachers | 25545 |
| diagnostics.groups.web.teacher_fraction | 0.8500549066586802 |
| diagnostics.groups.story.teachers | 1013 |
| diagnostics.groups.story.teacher_fraction | 0.03370936075338591 |
| diagnostics.groups.ordinary_textbook.teachers | 3048 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10142757312568633 |
| diagnostics.groups.conditional_outcome_body.teachers | 374 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.012445509300855213 |
| diagnostics.groups.conditional_EOS.teachers | 71 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0023626501613922997 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.5967215954417915 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.1768791526556015 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 74.86472417540114 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.10513338446617126 |
| diagnostics.groups.independent_total.teachers | 30051 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 445 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.014808159462247512 |
| diagnostics.pairs.web__story.dot | 0.0026311171241104603 |
| diagnostics.pairs.web__story.cosine | 0.036025886391660385 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.0010753222741186619 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.01066994125545696 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.0045170290395617485 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.05264379096885564 |
| diagnostics.pairs.web__conditional_EOS.dot | 0.0007137182401493192 |
| diagnostics.pairs.web__conditional_EOS.cosine | 0.008674080626766566 |
| diagnostics.pairs.web__independent_total.dot | 0.22534477710723877 |
| diagnostics.pairs.web__independent_total.cosine | 0.7646909386140953 |
| diagnostics.pairs.web__conditional_total.dot | 0.005230747163295746 |
| diagnostics.pairs.web__conditional_total.cosine | 0.04295764603561477 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.0031063526403158903 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.09132759470448913 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.004965942353010178 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.17148408957589353 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.00372689263895154 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.13420584966419363 |
| diagnostics.pairs.story__independent_total.dot | 0.03907860815525055 |
| diagnostics.pairs.story__independent_total.cosine | 0.39292115322970733 |
| diagnostics.pairs.story__conditional_total.dot | 0.00869283452630043 |
| diagnostics.pairs.story__conditional_total.cosine | 0.2115271181651626 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.0032024718821048737 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.08014129513580373 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.004866001196205616 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.12698301711218385 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.05278664082288742 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.3846265303975296 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.001663529546931386 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.029334861628957057 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.001604039454832673 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.04916537505776272 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.04189816862344742 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.3585759233025057 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.035625897347927094 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7378875803385304 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.04219008609652519 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.376529389919666 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.03289027139544487 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.7103857562945459 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.08408825099468231 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.507112020101635 |
| diagnostics.total_teacher_count | 30051 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/10.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/10.json) ／ SHA256: `5cfd38d7e01a2a88de381b26d265136da3a0544a7006330b3eee3ea29860912d` ／ 6,765 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320446 |
| input.reference_token_digest | "86dd4373b924ff67c22ab788363793db17099f19882f6a934693da9bc46790dd" |
| input.masked_token_digest | "4431b596f76f0e7d99b49a1c20c6be5edeff09ef8c154daedfd201ae3e664f6c" |
| input.teachers | 30109 |
| input.teachers_by_group.web | 23505 |
| input.teachers_by_group.story | 2033 |
| input.teachers_by_group.ordinary_textbook | 4064 |
| input.teachers_by_group.conditional_outcome_body | 433 |
| input.teachers_by_group.conditional_EOS | 74 |
| input.body_bytes | 117579 |
| diagnostics.groups.web.teachers | 23505 |
| diagnostics.groups.web.teacher_fraction | 0.7806635889601116 |
| diagnostics.groups.story.teachers | 2033 |
| diagnostics.groups.story.teacher_fraction | 0.06752133913447807 |
| diagnostics.groups.ordinary_textbook.teachers | 4064 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.13497625294762364 |
| diagnostics.groups.conditional_outcome_body.teachers | 433 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.014381082068484506 |
| diagnostics.groups.conditional_EOS.teachers | 74 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.002457736889302202 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.68606897302576 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.18355843424797058 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 74.68595806448846 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.08384586870670319 |
| diagnostics.groups.independent_total.teachers | 30109 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 507 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.01683881895778671 |
| diagnostics.pairs.web__story.dot | -0.0020290666725486517 |
| diagnostics.pairs.web__story.cosine | -0.019153742300502305 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.0013942496152594686 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.009623497866541982 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.0010096558835357428 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.01073236830598678 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.0015178939793258905 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.01752773947552445 |
| diagnostics.pairs.web__independent_total.dot | 0.22146648168563843 |
| diagnostics.pairs.web__independent_total.cosine | 0.663942285699582 |
| diagnostics.pairs.web__conditional_total.dot | -0.0005082378629595041 |
| diagnostics.pairs.web__conditional_total.cosine | -0.003915456285953394 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.012194721959531307 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.17684958651664803 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.011061547324061394 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.24704599265878632 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.0032733057159930468 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.07941650081479815 |
| diagnostics.pairs.story__independent_total.dot | 0.07491819560527802 |
| diagnostics.pairs.story__independent_total.cosine | 0.4718992931096091 |
| diagnostics.pairs.story__conditional_total.dot | 0.014334853738546371 |
| diagnostics.pairs.story__conditional_total.cosine | 0.23203225455546211 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.002311952644959092 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.037755129680623306 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.005348682403564453 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.09488686214647478 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.11092247068881989 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.5108773876041485 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.003036729758605361 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.03594151242225317 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0011211374076083302 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.030630064227325608 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.05064599961042404 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.35922955790544414 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.04088359326124191 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7451934822596843 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.04191356897354126 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.322956329044888 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.03481483832001686 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6893608631054464 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.0925595611333847 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.4758185806779371 |
| diagnostics.total_teacher_count | 30109 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/11.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/11.json) ／ SHA256: `d7a5c44fa46a923c8f98ddf38cd8aafe877d3a990570ebde23fe298a365056fa` ／ 6,756 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320447 |
| input.reference_token_digest | "b719c1d55c79af783a628171c16a4f62eca058bc4ee1aea31aaf8fe562dba54e" |
| input.masked_token_digest | "6812b2e51cbfbf1d299ad5e011c603612bc88474bb2a3eb22a1c69630cb94dc2" |
| input.teachers | 30081 |
| input.teachers_by_group.web | 24524 |
| input.teachers_by_group.story | 2036 |
| input.teachers_by_group.ordinary_textbook | 3050 |
| input.teachers_by_group.conditional_outcome_body | 403 |
| input.teachers_by_group.conditional_EOS | 68 |
| input.body_bytes | 117804 |
| diagnostics.groups.web.teachers | 24524 |
| diagnostics.groups.web.teacher_fraction | 0.8152654499517968 |
| diagnostics.groups.story.teachers | 2036 |
| diagnostics.groups.story.teacher_fraction | 0.06768392008244407 |
| diagnostics.groups.ordinary_textbook.teachers | 3050 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.1013929058209501 |
| diagnostics.groups.conditional_outcome_body.teachers | 403 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.013397160998637013 |
| diagnostics.groups.conditional_EOS.teachers | 68 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.002260563146172002 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.472309785730698 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.16977323591709137 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 75.10218690620626 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.08574387431144714 |
| diagnostics.groups.independent_total.teachers | 30081 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 471 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.015657724144809017 |
| diagnostics.pairs.web__story.dot | -0.002397575881332159 |
| diagnostics.pairs.web__story.cosine | -0.02336082676706635 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.005198175087571144 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.04848336105003384 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.0038031069561839104 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.043674314026783616 |
| diagnostics.pairs.web__conditional_EOS.dot | 0.0017071218462660909 |
| diagnostics.pairs.web__conditional_EOS.cosine | 0.020865756408433907 |
| diagnostics.pairs.web__independent_total.dot | 0.24054506421089172 |
| diagnostics.pairs.web__independent_total.cosine | 0.7530772323387507 |
| diagnostics.pairs.web__conditional_total.dot | 0.005510229151695967 |
| diagnostics.pairs.web__conditional_total.cosine | 0.045132973823476516 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.003991811536252499 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.08424613947902239 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.006243020296096802 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.1622260046122442 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.0016714958474040031 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.04622884915303884 |
| diagnostics.pairs.story__independent_total.dot | 0.05486585199832916 |
| diagnostics.pairs.story__independent_total.cosine | 0.3886720735444029 |
| diagnostics.pairs.story__conditional_total.dot | 0.007914516143500805 |
| diagnostics.pairs.story__conditional_total.cosine | 0.14668537859638778 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.0003071372047998011 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.007639837699174677 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.0041113486513495445 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.10884739877882571 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.06250229477882385 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.42384115998135463 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.003804211737588048 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.06749212283161418 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0013549672439694405 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.044168056375402415 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.04373866692185402 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.3651896605340605 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.034006424248218536 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7428397191760165 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.037669919431209564 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.3347570077901634 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.03017791546881199 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.701625657490739 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.08140860497951508 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.48479704637254034 |
| diagnostics.total_teacher_count | 30081 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/12.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/12.json) ／ SHA256: `4e04caf777f184934cdb133e257b2e2e77cf5d0461acf602005a2d640cb4231b` ／ 6,770 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320448 |
| input.reference_token_digest | "89514be684433853f9230b1dc8ffed7db5cc91857b393862a0e8b6194fe64f04" |
| input.masked_token_digest | "ebc667d3a48ef9ac42787e5809ab9b80bff9b14848ebea8f1f82d68224f3794f" |
| input.teachers | 29218 |
| input.teachers_by_group.web | 24527 |
| input.teachers_by_group.story | 1018 |
| input.teachers_by_group.ordinary_textbook | 3049 |
| input.teachers_by_group.conditional_outcome_body | 530 |
| input.teachers_by_group.conditional_EOS | 94 |
| input.body_bytes | 114750 |
| diagnostics.groups.web.teachers | 24527 |
| diagnostics.groups.web.teacher_fraction | 0.83944828530358 |
| diagnostics.groups.story.teachers | 1018 |
| diagnostics.groups.story.teacher_fraction | 0.03484153603942775 |
| diagnostics.groups.ordinary_textbook.teachers | 3049 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.1043534807310562 |
| diagnostics.groups.conditional_outcome_body.teachers | 530 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.01813950304606749 |
| diagnostics.groups.conditional_EOS.teachers | 94 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0032171948798685743 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.655154126755734 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.23853404819965363 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 74.14348744997318 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.15461494028568268 |
| diagnostics.groups.independent_total.teachers | 29218 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 624 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.02135669792593607 |
| diagnostics.pairs.web__story.dot | 0.002808147110044956 |
| diagnostics.pairs.web__story.cosine | 0.04575645204328969 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.002227102406322956 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.01984579466833108 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.001343805342912674 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.010831738162394307 |
| diagnostics.pairs.web__conditional_EOS.dot | 0.009629647247493267 |
| diagnostics.pairs.web__conditional_EOS.cosine | 0.08243576411600011 |
| diagnostics.pairs.web__independent_total.dot | 0.2531507611274719 |
| diagnostics.pairs.web__independent_total.cosine | 0.7455900509463815 |
| diagnostics.pairs.web__conditional_total.dot | 0.008285840973258018 |
| diagnostics.pairs.web__conditional_total.cosine | 0.048164212332163614 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.002893623895943165 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.10076078649456091 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.004275220446288586 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.13466088739873336 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.0008894503116607666 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.02975419021147458 |
| diagnostics.pairs.story__independent_total.dot | 0.02657276764512062 |
| diagnostics.pairs.story__independent_total.cosine | 0.30582910394833207 |
| diagnostics.pairs.story__conditional_total.dot | 0.00516467122361064 |
| diagnostics.pairs.story__conditional_total.cosine | 0.117314499600301 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.0024843220598995686 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.04279437603920952 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.005735530983656645 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.10492909403729514 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.06088331341743469 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.3832093956883843 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.0032512089237570763 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.04038775616735568 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0011645308695733547 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.019271111036312075 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.06576956808567047 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.3744521467161296 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.06534276902675629 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7342363468406388 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.07432262599468231 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.44940289335875416 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.058063022792339325 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6929174191786162 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.14009219408035278 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.575190022482843 |
| diagnostics.total_teacher_count | 29218 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/13.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/13.json) ／ SHA256: `f8b7cbb517041eb7fbe9e2aa8b817b15572126cd7ef941b3facbcdc53bfe3bc0` ／ 6,754 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320449 |
| input.reference_token_digest | "bafa83fd10434309d3b4cb37b107bd91caeb82ca7c409aa55cbff0fc8d2e42d7" |
| input.masked_token_digest | "a3a8dde0b7640f4af1286fb50f11ae7c9d6e7b8debd192b574378797017a3a43" |
| input.teachers | 30121 |
| input.teachers_by_group.web | 24522 |
| input.teachers_by_group.story | 2030 |
| input.teachers_by_group.ordinary_textbook | 3047 |
| input.teachers_by_group.conditional_outcome_body | 446 |
| input.teachers_by_group.conditional_EOS | 76 |
| input.body_bytes | 119192 |
| diagnostics.groups.web.teachers | 24522 |
| diagnostics.groups.web.teacher_fraction | 0.8141163971979682 |
| diagnostics.groups.story.teachers | 2030 |
| diagnostics.groups.story.teacher_fraction | 0.06739484080873809 |
| diagnostics.groups.ordinary_textbook.teachers | 3047 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10115866007104678 |
| diagnostics.groups.conditional_outcome_body.teachers | 446 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.014806945320540487 |
| diagnostics.groups.conditional_EOS.teachers | 76 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0025231566017064506 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.680743568821957 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.18760332465171814 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 74.35262818203161 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.09826330095529556 |
| diagnostics.groups.independent_total.teachers | 30121 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 522 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.01733010192224694 |
| diagnostics.pairs.web__story.dot | 0.002058285754173994 |
| diagnostics.pairs.web__story.cosine | 0.019529344621574216 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.006385797634720802 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.060104430108118057 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.0005292634014040232 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.005343473032159063 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.00048502784920856357 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.0055613326368212845 |
| diagnostics.pairs.web__independent_total.dot | 0.21077725291252136 |
| diagnostics.pairs.web__independent_total.cosine | 0.6700798286720578 |
| diagnostics.pairs.web__conditional_total.dot | -0.0010142908431589603 |
| diagnostics.pairs.web__conditional_total.cosine | -0.0075662028376078634 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.011967508122324944 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.23097851740353825 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.009977513924241066 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.20656208577291962 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.004930746741592884 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.11593148817489181 |
| diagnostics.pairs.story__independent_total.dot | 0.08034095168113708 |
| diagnostics.pairs.story__independent_total.cosine | 0.5237406513392878 |
| diagnostics.pairs.story__conditional_total.dot | 0.01490826066583395 |
| diagnostics.pairs.story__conditional_total.cosine | 0.22804417653656217 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | 0.001856014714576304 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | 0.03811702741216435 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.004064618144184351 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.09480206856966897 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.0637340247631073 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.4121544531496327 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.0059206318110227585 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.08983992819622988 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0012814877554774284 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.03206069650470798 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.05797645449638367 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.40216171272444584 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.04667585715651512 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7597208325908098 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.04498743265867233 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.35440576730490225 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.0364765003323555 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6742723840936882 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.102963887155056 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.5277129529830094 |
| diagnostics.total_teacher_count | 30121 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/14.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/14.json) ／ SHA256: `b264cfcbb1f04ae9815c1a6efdac92709a89f99b460d24a7ea41fe050a1d041f` ／ 6,744 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320450 |
| input.reference_token_digest | "dc7353b5dd8461912c8cf47fdb2ce71ab7e356514d08b7158ceab7299ebfffd3" |
| input.masked_token_digest | "211f09467752625c85171233ee53695c8649abd4ba2d692b222fc25036b8ef0e" |
| input.teachers | 30093 |
| input.teachers_by_group.web | 25543 |
| input.teachers_by_group.story | 1015 |
| input.teachers_by_group.ordinary_textbook | 3048 |
| input.teachers_by_group.conditional_outcome_body | 418 |
| input.teachers_by_group.conditional_EOS | 69 |
| input.body_bytes | 117837 |
| diagnostics.groups.web.teachers | 25543 |
| diagnostics.groups.web.teacher_fraction | 0.8488020469876716 |
| diagnostics.groups.story.teachers | 1015 |
| diagnostics.groups.story.teacher_fraction | 0.03372877413351942 |
| diagnostics.groups.ordinary_textbook.teachers | 3048 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.10128601335858838 |
| diagnostics.groups.conditional_outcome_body.teachers | 418 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.013890273485528196 |
| diagnostics.groups.conditional_EOS.teachers | 69 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.0022928920346924533 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.626406241154325 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.1724177896976471 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 75.19664558509122 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.07845974713563919 |
| diagnostics.groups.independent_total.teachers | 30093 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 487 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.01618316552022065 |
| diagnostics.pairs.web__story.dot | 0.0026577827520668507 |
| diagnostics.pairs.web__story.cosine | 0.04077090905745231 |
| diagnostics.pairs.web__ordinary_textbook.dot | 0.0029066898860037327 |
| diagnostics.pairs.web__ordinary_textbook.cosine | 0.025950672980567725 |
| diagnostics.pairs.web__conditional_outcome_body.dot | 0.0033503989689052105 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | 0.035424207988402914 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.002052520401775837 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.02328028132938079 |
| diagnostics.pairs.web__independent_total.dot | 0.2683786153793335 |
| diagnostics.pairs.web__independent_total.cosine | 0.7865164103664131 |
| diagnostics.pairs.web__conditional_total.dot | 0.0012978785671293736 |
| diagnostics.pairs.web__conditional_total.cosine | 0.009969456796694367 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.005753857083618641 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.20605078192250167 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.00512358546257019 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.21729157157656273 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.002801420632749796 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.12745131728114703 |
| diagnostics.pairs.story__independent_total.dot | 0.03259328007698059 |
| diagnostics.pairs.story__independent_total.cosine | 0.3831362444451062 |
| diagnostics.pairs.story__conditional_total.dot | 0.007925005629658699 |
| diagnostics.pairs.story__conditional_total.cosine | 0.24417562029785866 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | 0.0027807955630123615 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | 0.06863678810736247 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.0040169223211705685 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.1063600309132122 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.06343342363834381 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.4339726144144791 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.006797717418521643 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.12189470499217295 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0004394734569359571 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.013780702830954589 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.045904893428087234 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.37192626247412963 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.03464989736676216 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7358297998513668 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.034937575459480286 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.3036601233629248 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.030167367309331894 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.6872424641293491 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.08084246516227722 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.475851270285475 |
| diagnostics.total_teacher_count | 30093 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/15.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/points/original_fullparent/15.json) ／ SHA256: `72bc9dcadfcb82f80a1b2914f3434df58fb584cca6c003c284d1e85a9254f9bd` ／ 6,793 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| input.update | 320451 |
| input.reference_token_digest | "8df15572536212e7143ef5ed7c26a0c70244e20de9546a3d0f74ffd26ec573a3" |
| input.masked_token_digest | "83950ca52e867264576e3f491e376baaa850aab75a4159dd6871d0da3a643770" |
| input.teachers | 30027 |
| input.teachers_by_group.web | 23501 |
| input.teachers_by_group.story | 2029 |
| input.teachers_by_group.ordinary_textbook | 4067 |
| input.teachers_by_group.conditional_outcome_body | 366 |
| input.teachers_by_group.conditional_EOS | 64 |
| input.body_bytes | 119949 |
| diagnostics.groups.web.teachers | 23501 |
| diagnostics.groups.web.teacher_fraction | 0.7826622706231059 |
| diagnostics.groups.story.teachers | 2029 |
| diagnostics.groups.story.teacher_fraction | 0.06757251806707297 |
| diagnostics.groups.ordinary_textbook.teachers | 4067 |
| diagnostics.groups.ordinary_textbook.teacher_fraction | 0.13544476637692743 |
| diagnostics.groups.conditional_outcome_body.teachers | 366 |
| diagnostics.groups.conditional_outcome_body.teacher_fraction | 0.012189029873114198 |
| diagnostics.groups.conditional_EOS.teachers | 64 |
| diagnostics.groups.conditional_EOS.teacher_fraction | 0.002131415059779532 |
| diagnostics.groups.conditional_EOS.CE_mean | 6.474225997924805 |
| diagnostics.groups.conditional_EOS.contribution_gradient_norm | 0.16246727108955383 |
| diagnostics.groups.conditional_EOS.group_mean_gradient_norm | 76.22507420321926 |
| diagnostics.groups.conditional_EOS.contribution_to_total_squared_norm | 0.0758863165974617 |
| diagnostics.groups.independent_total.teachers | 30027 |
| diagnostics.groups.independent_total.teacher_fraction | 1.0 |
| diagnostics.groups.conditional_total.teachers | 430 |
| diagnostics.groups.conditional_total.teacher_fraction | 0.01432044493289373 |
| diagnostics.pairs.web__story.dot | -0.0025478906463831663 |
| diagnostics.pairs.web__story.cosine | -0.022752843223044897 |
| diagnostics.pairs.web__ordinary_textbook.dot | -0.0019850307144224644 |
| diagnostics.pairs.web__ordinary_textbook.cosine | -0.015295378467542956 |
| diagnostics.pairs.web__conditional_outcome_body.dot | -0.002223790157586336 |
| diagnostics.pairs.web__conditional_outcome_body.cosine | -0.02811822502846707 |
| diagnostics.pairs.web__conditional_EOS.dot | -0.0013312604278326035 |
| diagnostics.pairs.web__conditional_EOS.cosine | -0.017335180504751444 |
| diagnostics.pairs.web__independent_total.dot | 0.21532493829727173 |
| diagnostics.pairs.web__independent_total.cosine | 0.6840381726517314 |
| diagnostics.pairs.web__conditional_total.dot | -0.003555051051080227 |
| diagnostics.pairs.web__conditional_total.cosine | -0.031826905375245296 |
| diagnostics.pairs.story__ordinary_textbook.dot | 0.011981824412941933 |
| diagnostics.pairs.story__ordinary_textbook.cosine | 0.184207959606905 |
| diagnostics.pairs.story__conditional_outcome_body.dot | 0.0076268138363957405 |
| diagnostics.pairs.story__conditional_outcome_body.cosine | 0.19241090489382476 |
| diagnostics.pairs.story__conditional_EOS.dot | 0.004192410036921501 |
| diagnostics.pairs.story__conditional_EOS.cosine | 0.10892347869413951 |
| diagnostics.pairs.story__independent_total.dot | 0.0773824155330658 |
| diagnostics.pairs.story__independent_total.cosine | 0.49047932619145845 |
| diagnostics.pairs.story__conditional_total.dot | 0.011819223873317242 |
| diagnostics.pairs.story__conditional_total.cosine | 0.2111202847766025 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.dot | -0.003006467130035162 |
| diagnostics.pairs.ordinary_textbook__conditional_outcome_body.cosine | -0.0654456974794836 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.dot | 0.0036771688610315323 |
| diagnostics.pairs.ordinary_textbook__conditional_EOS.cosine | 0.08243459023745357 |
| diagnostics.pairs.ordinary_textbook__independent_total.dot | 0.08605089038610458 |
| diagnostics.pairs.ordinary_textbook__independent_total.cosine | 0.47062164628409314 |
| diagnostics.pairs.ordinary_textbook__conditional_total.dot | 0.0006707013817504048 |
| diagnostics.pairs.ordinary_textbook__conditional_total.cosine | 0.010337329157636434 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.dot | 0.0007261729915626347 |
| diagnostics.pairs.conditional_outcome_body__conditional_EOS.cosine | 0.026713886887108226 |
| diagnostics.pairs.conditional_outcome_body__independent_total.dot | 0.031106753274798393 |
| diagnostics.pairs.conditional_outcome_body__independent_total.cosine | 0.2791722926358529 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.dot | 0.02872077189385891 |
| diagnostics.pairs.conditional_outcome_body__conditional_total.cosine | 0.7264007738804239 |
| diagnostics.pairs.conditional_EOS__independent_total.dot | 0.03365533798933029 |
| diagnostics.pairs.conditional_EOS__independent_total.cosine | 0.31105903468429125 |
| diagnostics.pairs.conditional_EOS__conditional_total.dot | 0.027121789753437042 |
| diagnostics.pairs.conditional_EOS__conditional_total.cosine | 0.7064311045677554 |
| diagnostics.pairs.independent_total__conditional_total.dot | 0.06476209312677383 |
| diagnostics.pairs.independent_total__conditional_total.cosine | 0.4115219134581761 |
| diagnostics.total_teacher_count | 30027 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/result.json — fixed_TRAIN_gradient_attribution_complete</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/result.json) ／ SHA256: `8c7c9d08bd8a4ac87fe2eb1501d49e7f5de6b42f7da3cdfc465ea4e9e527c7a7` ／ 273,337 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_TRAIN_gradient_attribution_complete" |
| models.original_fullparent.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| models.original_fullparent.checkpoint.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| models.original_fullparent.read_only_checks.weights_unchanged | true |
| models.original_fullparent.read_only_checks.no_gradients | true |
| models.original_fullparent.read_only_checks.eval_mode | true |
| models.original_fullparent.read_only_checks.finite_weights | true |
| models.original_fullparent.read_only_checks.RNG_unchanged_during_gradients | true |
| models.completed_masked_mixed.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/interleaved-outcome-order-20261006/interleaved_outcome_EOS/training/checkpoint-00323503.pt" |
| models.completed_masked_mixed.checkpoint.sha256 | "32e1bf47d5aaee27364aa108831e5bb1ea8dae3e4f5bbd80267fef86a99ad192" |
| models.completed_masked_mixed.read_only_checks.weights_unchanged | true |
| models.completed_masked_mixed.read_only_checks.no_gradients | true |
| models.completed_masked_mixed.read_only_checks.eval_mode | true |
| models.completed_masked_mixed.read_only_checks.finite_weights | true |
| models.completed_masked_mixed.read_only_checks.RNG_unchanged_during_gradients | true |
| GPU_seconds | 36.00103650402161 |
| distinct_logical_input_tokens | 524288 |
| gradient_teacher_targets_per_model | 478111 |
| new_teacher_tokens | 0 |
| optimizer_updates | 0 |
| limitations | "Local unchanged token-mean CE at16 fixed TRAIN batches/two preselected endpoints/one learned seed; BF16/math eager8-sequence chunks. Not optimizer directions, GPU learning, model quality, causal dilution proof or an automatic reweighting recommendation." |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-20261006/samples.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-20261006/samples.json) ／ SHA256: `4204dcd5e8a430e2af231097b2ba5f8a392195dbcfe10f0e77a719ee3eb3f37c` ／ 20,984 bytes

| 原キー | 保存値 |
|---|---|
| seed | 42 |

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/source-gradient-attribution-launcher-20261006/launcher.json) ／ SHA256: `83f6ec51eb4e60f0ec71fbaef4eefdd743bae3499677f87e01618aa3ce55b166` ／ 83 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/source-gradient-attribution-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/source-gradient-attribution-launcher-20261006/result.json) ／ SHA256: `d1d157575485bd4eba09adda62e9befc762f5e1b796ae6591e01c800efeac47b` ／ 155 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-20261006/probe/initial-parent-preservation.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-20261006/probe/initial-parent-preservation.json) ／ SHA256: `32d3d22cad0f3d58b45aa7f07a08fe830334be2c9dd6a9572917b1c6c1fb7b34` ／ 161 bytes

| 原キー | 保存値 |
|---|---|
| parent_sampler_lineage | true |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-20261006/probe/job.json) ／ SHA256: `6242e89cd89ebe5c1634c7a8e7ef2ae011a4317f29345fee7c6584257e184477` ／ 603 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 20.29770903699682 |
| Base_adopted | false |
| protected_test_used | false |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-20261006/probe/result.json — actual_source_order_resume_timing_complete</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-20261006/probe/result.json) ／ SHA256: `47b9b73423a2fcd70c5dbfcde36f6ab1110b6ccf9272236e87ca8d43b018e9bb` ／ 67,133 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_source_order_resume_timing_complete" |
| passed | true |
| gate.passed | true |
| gate.checks.model | true |
| gate.checks.optimizer | true |
| gate.checks.scheduler | true |
| gate.checks.rng | true |
| gate.checks.sampler | true |
| gate.checks.lineage | true |
| gate.checks.tokens | true |
| gate.checks.supervised_tokens | true |
| gate.checks.body_bytes | true |
| gate.checks.token_digest | true |
| gate.checks.focus_token_digest | true |
| gate.checks.focus_teacher_tokens | true |
| gate.checks.weighted_teacher_mass | true |
| gate.checks.update | true |
| gate.checks.spec | true |
| gate.checks.model_config | true |
| gate.checks.pilot_binding | true |
| gate.checks.study_binding | true |
| gate.checks.history_loss | true |
| gate.checks.history_gradient_norm | true |
| gate.checks.history_lr | true |
| gate.checks.history_token_digest | true |
| gate.checks.history_source_teachers | true |
| gate.checks.history_source_eos | true |
| gate.checks.history_source_input_tokens | true |
| gate.checks.history_source_body_bytes | true |
| gate.checks.history_source_focus_teachers | true |
| gate.checks.history_focus_token_digest | true |
| gate.checks.history_focus_teacher_tokens | true |
| gate.checks.history_weighted_teacher_mass | true |
| gate.checks.finite | true |
| gate.checks.no_reheat | true |
| gate.GPU_optimizer_updates | 8 |
| gate.verification_teacher_tokens | 261602 |
| timing.verification_teacher_tokens | 1046365 |
| timing.terminal_save_seconds | 0.16663748701103032 |
| timing.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-20261006/probe/timing/checkpoint.pt" |
| timing.checkpoint_sha256 | "c479999ac4f33a05283f4e92926c67a49b71f527b698e9903f55f638343caf96" |
| verification_teacher_tokens | 1307967 |
| GPU_optimizer_updates | 40 |
| scientific_teacher_tokens | 0 |
| initial_parent_preservation.parent_sampler_lineage | true |
| GPU_seconds | 20.29770903699682 |

</details>

<details>
<summary>reports/phase6/source-order-condition-comparison-20261006/probe/timing/latest.json — None</summary>

[原記録](../../reports/phase6/source-order-condition-comparison-20261006/probe/timing/latest.json) ／ SHA256: `19e301f399483626ae53388d6933b270404a15363cc33d0fedb5d58eaca21a1d` ／ 276 bytes

| 原キー | 保存値 |
|---|---|
| update | 320467 |
| tokens_seen | 10501062656 |

</details>

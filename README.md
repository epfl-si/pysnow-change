<h1 align="center">PYSNOW CHANGE EPFL</h1>
<p align="center">
  ServiceNow change creation tool for EPFL-IDevelop.
</p>

<p align="center">
  <a href="https://travis-ci.org/epfl-idevelop/pysnow-change">
    <img alt="Travis Status" src="https://travis-ci.org/epfl-idevelop/pysnow-change.svg?branch=master">
  </a>
  <a href="https://raw.githubusercontent.com/epfl-idevelop/pysnow-change/master/LICENSE">
    <img alt="Apache License 2.0" src="https://img.shields.io/badge/license-Apache%202.0-blue.svg">
  </a>
</p>

---

Description
-----------
This tool offer the possibility to create a **Standard Change** in the ServiceNow of the EPFL with a unique command. This change is created directly closed.
It could be used for every new deployment in production, unless the change need an approval by the Management (which in this case must be done manually one week in advance).  

##### Details
* The usage is reserved for the unit **IDevelop** of the VPSI, EPFL.
* The planned and work start date is set to current date.
* The planned and work end date is set to current date plus 1 minute.

Install
-------

```bash
$ pip install pysnow-change-epfl
```

Usage
-----
1. Create an environment variable **'SCIPER'** with your Sciper number (ex: SCIPER=123456)
2. Create an environment variable **'SNOW_CHG_PWD'** with the password of user 'idevelop_webservice'
3. See an implementation example in example/example1.py

API
---  
### create_change()

**Parameters:**

| Name              | Type   | Required            | Description                             | Possible values                       | Example                                      |
|-------------------|--------|---------------------|-----------------------------------------|---------------------------------------|----------------------------------------------|
| service_id        | String | yes                 | Business Service ID                     | &lt;All existing Business Service&gt; | 'SVC0016'                                    |
| snow_group        | String | yes                 | Assignement group                       | &lt;All existing assignable group&gt; | 'SI_NEWS'                                    |
| impact_category   | String | yes                 | Impact                                  | 'Minor', 'Significant' or 'Major'     | 'Minor'                                      |
| short_description | String | yes                 | Short description (title of the change) | &lt;free text&gt;                     | 'Actu - v1.4.3'                              |
| description       | String | yes                 | Description (list of changes)           | &lt;free text&gt;                     | '- Fix unit test<br>- Update dependencies'   |
| env               | String | no (default:'test') | ServiceNow environment                  | 'test', 'prod'                        | 'prod'                                       |

**Return value:**  
A string who contains a confirmation message with the Change Number and URL or an error message.


Contributing
------------
Contributions are welcome.

Developer
---------

  * [Olivier Bieler](https://github.com/obieler)

License
-------

Apache License 2.0

(c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2018.

See the [LICENSE](LICENSE) file for more details.

from pyelt.datalayers.database import DbFunction, DbFunctionParameter


class CreateAdresnl_bk(DbFunction):
    def __init__(self, wijkcode='', lettercombinatie='', huisnr='', huisnr_bag_letter='', huisnr_bag_toevoeging=''):
        super().__init__()
        self.name = 'create_adresnl_bk'
        param1 = DbFunctionParameter('wijkcode', 'text', wijkcode)
        param2 = DbFunctionParameter('lettercombinatie', 'text', lettercombinatie)
        param3 = DbFunctionParameter('huisnr', 'text', huisnr)
        param4 = DbFunctionParameter('huisnr_bag_letter', 'text', huisnr_bag_letter)
        param5 = DbFunctionParameter('huisnr_bag_toevoeging', 'text', huisnr_bag_toevoeging)

        self.func_params.append(param1)
        self.func_params.append(param2)
        self.func_params.append(param3)
        self.func_params.append(param4)
        self.func_params.append(param5)

        self.return_type = 'text'
        self.schema = 'sor_adresnl'
        self.sql_body = """
            DECLARE
                    bk text;
                    bk_begin text;
                    bk_end text;

        BEGIN

            bk_begin := wijkcode || lettercombinatie || '.' || huisnr;


            bk_end :=  case
                    WHEN huisnr_bag_letter is not NULL and huisnr_bag_toevoeging is not NULL
                        THEN '-' || huisnr_bag_letter ||'-' || huisnr_bag_toevoeging
                    WHEN huisnr_bag_letter is not NULL
                        THEN '-' || huisnr_bag_letter
                    WHEN huisnr_bag_toevoeging is not NULL
                        THEN '-' || huisnr_bag_toevoeging
                end;

            bk = bk_begin || bk_end;

            return bk;

        END;"""

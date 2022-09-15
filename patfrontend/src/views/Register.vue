<template>
    <section class="py-100-70 login">
        <div class="text-center mb-4">
            <h2>Welcome Please Register</h2>
        </div>
        <div class="container add-comments">
            <form class="inner-add-comments form-contact-1" @submit.prevent="registerUser">
                <div class="row">
                    <div class="col-md-6 offset-md-3">

                        <div class="mb-3">
                            <div class="form-group">
                                <label for="firstname">First Name <span style="color: red">*</span></label>
                                <input type="text" v-model="firstname" class="form-control" id="firstname">
                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="middlename">Middle name <span style="color: red">*</span></label>
                                <input type="text" v-model="middlename" class="form-control" id="middlename">
                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="lastname">Last Name <span style="color: red">*</span></label>
                                <input type="text" v-model="lastname" class="form-control" id="lastname">
                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="username">Username <span style="color: red">*</span></label>
                                <input type="text" v-model="username" class="form-control" id="username">
                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="email">Email <span style="color: red">*</span></label>
                                <input type="email" v-model="email" class="form-control" id="email">
                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="phonenumber">Phone Number (Start with +255)</label>
                                <input type="phone" v-model="phonenumber" class="form-control" id="phonenumber">
                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="mct">MCT number (optional)</label>
                                <input type="text" v-model="mct" class="form-control" id="mct">
                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="password">Password</label>
                                <input type="password" v-model="password" class="form-control" id="password">
                            </div>
                        </div>
                        <div class="mb-3">
                            <div class="form-group">
                                <label for="confirmpass">Confrim Password</label>
                                <input type="password" v-model="repassword" class="form-control" id="confirmpass">
                            </div>
                        </div>

                        <div class="mb-3">
                            <label for="gender">Gender <span style="color: red">*</span></label>
                            <select name="gender" class="form-control" v-model="gender" id="gender">
                                <option value="Male">Male</option>
                                <option value="Female">Female</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label for="region">Region <span style="color: red">*</span></label>
                            <select class="form-control" v-model="region" id="region">
                                <option value="Arusha">Arusha</option>
                                <option value="Dar es Salaam">Dar es Salaam</option>
                                <option value="Dodoma">Dodoma</option>
                                <option value="Geita">Geita</option>
                                <option value="Iringa">Iringa</option>
                                <option value="Kagera">Kagera</option>
                                <option value="Katavi">Katavi</option>
                                <option value="Kigoma">Kigoma</option>
                                <option value="Kilimanjaro">Kilimanjaro</option>
                                <option value="Lindi">Lindi</option>
                                <option value="Manyara">Manyara</option>
                                <option value="Mara">Mara</option>
                                <option value="Mbeya">Mbeya</option>
                                <option value="Mjini Magharibi">Mjini Magharibi</option>
                                <option value="Morogoro">Morogoro</option>
                                <option value="Mtwara">Mtwara</option>
                                <option value="Mwanza">Mwanza</option>
                                <option value="Njombe">Njombe</option>
                                <option value="Pemba North">Pemba North</option>
                                <option value="Pemba South">Pemba South</option>
                                <option value="Pwani">Pwani</option>
                                <option value="Rukwa">Rukwa</option>
                                <option value="Ruvuma">Ruvuma</option>
                                <option value="Shinyanga">Shinyanga</option>
                                <option value="Simiyu">Simiyu</option>
                                <option value="Singida">Singida</option>
                                <option value="Songwe">Songwe</option>
                                <option value="Tabora">Tabora</option>
                                <option value="Tanga">Tanga</option>
                                <option value="Unguja North">Unguja North</option>
                                <option value="Unguja South">Unguja South</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label>Please select the profession that most closely represents you <span
                                    style="color: red">*</span></label>
                            <select class="form-control" name="profession">
                                <option value="Administrator">Administrator</option>
                                <option value="Community health worker">ommunity health worker</option>
                                <option value="First responder such as EMT or Paramedic">First responder such as EMT or
                                    Paramedic</option>
                                <option value="Mental health provider such as counselor, psychologist, social worker">
                                    Mental
                                    health provider such as counselor, psychologist, social worker</option>
                                <option value="Nurse or practitioner or physician assistant">Nurse or practitioner or
                                    physician
                                    assistant</option>
                                <option value="Pharmacist">Pharmacist</option>
                                <option value="Paediatrician">Paediatrician</option>
                                <option value="Public health official">Public health official</option>
                                <option value="Testing or laboratory personnel">Testing or laboratory personnel</option>
                                <option value="Teacher/educator">Teacher/educator</option>
                                <option value="Researcher">Researcher</option>
                                <option value="Student">Student</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label>Your organization Name<span style="color: red">*</span></label>
                            <input type="text" v-model="organization" class="form-control"
                                placeholder="Bugando Medical Center">
                        </div>

                        <div class="mb-3">
                            <label>Area of work or Industry <span style="color: red">*</span></label>
                            <select class="form-control" v-model="industry">
                                <option value="">Work</option>
                                <option value="Hospital">Hospital</option>
                                <option value="Community healthcare">Community healthcare</option>
                                <option value="Nursing/care facility">Nursing/care facility</option>
                                <option value="Public health">Public health</option>
                                <option value="Non-governmental organization">Non-governmental organization
                                </option>
                                <option value="School/university">School/university</option>
                                <option value="Government">Government</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <div class="form-group">
                                <label class="control-label ">Membership type</label>
                                <select class="form-control" v-model="typeofmember">
                                    <option value="Associate Member">Associate Member</option>
                                    <option value="Ordinary Member">Ordinary Member</option>
                                </select>
                            </div>
                        </div>


                        <button class="btn btn-primary btn-user mt-4 btn-block">
                            Register To PAT
                        </button>

                    </div>
                </div>
            </form>
        </div>
    </section>
</template>

<script>
import axios from 'axios';
import router from '../router';

export default {
    data() {
        return {
            firstname: '',
            middlename: '',
            lastname: '',
            username: '',
            email: '',
            mct: 0,
            password: '',
            repassword: '',
            gender: 'Female',
            region: 'Dodoma',
            phonenumber: '',
            profession: 'Researcher',
            organization: '',
            industry: 'Hospital',
            typeofmember: 'Associate Member',
        }
    },
    methods: {
        async registerUser() {
            const data = {
                first_name: this.firstname,
                middlename: this.middlename,
                last_name: this.lastname,
                username: this.username,
                email: this.email,
                phone_number: this.phonenumber,
                password: this.password,
                mctnumber: this.mct,
                gender: this.gender,
                region: this.region,
                profession: this.profession,
                organization: this.organization,
                areaofwork: this.industry,
                typeofmember: this.typeofmember,
            }
            axios.post('http://localhost:8000/api/v1/user/', data).
            then(response => {
                router.push({name: 'login'})
            }).catch(error => {
                console.log(error)
            })
        },
    }
}
</script>